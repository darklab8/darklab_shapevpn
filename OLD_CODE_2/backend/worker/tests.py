from django.conf import settings

from rest_framework import status as rest_status
import pytest
from rest_framework.reverse import reverse

# from furl import furl
from rest_framework.test import APIClient
import time

# Create your tests here.
import asyncio

from celery.result import ResultBase
from celery.result import AsyncResult
from core.celery import TaskStatus
from core.celery import (
    debug_task,
    debug_task_can_input_which_data,
    task_vpn_install,
    task_get_id,
)
from .models import is_input_verified
from core.encryptor import SymmetricEncryptor

def assert_task(id):
    for second in range(10):
        if TaskStatus.PENDING != AsyncResult(id).status:
            print(AsyncResult(id).status)
            break
        time.sleep(1)
    assert TaskStatus.PENDING != AsyncResult(id).status


@pytest.fixture
def client():
    return APIClient()


def test_ping_test(client):
    resp = client.get(reverse(viewname="ping"), follow=True, format="json")
    print(reverse(viewname="ping"))
    assert resp.status_code == 200


def test_ping_post(client):
    resp = client.post(reverse(viewname="ping"), follow=True, format="json")
    assert resp.status_code == 200

@pytest.mark.integration
def test_send_job():

    print("starting task")
    task = debug_task.delay()
    print("the task is sent")
    task = AsyncResult(task.id)
    print(task.id)
    print(AsyncResult(task.id).status)

    assert_task(task.id)

@pytest.mark.integration
def test_inputting_data():

    task = debug_task_can_input_which_data.delay({"data": 123, "bla": 467})
    assert_task(task.id)

# @pytest.mark.integration
# def test_inputting_data_async():

#     task = debug_task_can_input_which_data.apply_async(kwargs={"data": 123, "bla": 467})
#     assert_task(task.id)

@pytest.mark.integration
def test_to_get_task_id():

    task = task_get_id.delay()


# @pytest.mark.skip(reason="you already invoke test via request")
# DISABLED because ut is repeating next test
# def test_ssh_vpnserver_installation():

#     task = task_vpn_install.delay(
#         auth="ssh",
#         ip_address="wireguard-ssh.light-search.com",
#         user="root",
#         start=measurer.start_time_measuring(),
#         server_ssh_port="22000",
#         server_vpn_port="31289"
#     )
#     assert_task(task.id)

#     for i in range(10):
#         task = AsyncResult(task.id)
#         print(task.status)
#         print(dir(task))
#         time.sleep(2)


@pytest.mark.integration
@pytest.mark.longtests
def test_send_request_to_install_vpn(client):
    url = reverse(viewname="install")
    data_key = SymmetricEncryptor.generate_key()
    response = client.post(
        reverse(viewname="install"),
        data={
            "auth": "ssh",
            "ip_address": "wireguard-ssh.light-search.com",
            "user": "root",
            "server_ssh_port": "22000",
            "server_vpn_port": "31289",
            "private_key": settings.TEST_PRIVATE_KEY,
            "data_key": data_key
        },
        format="json",
    )
    print(response.json())
    task_id = response.json()["task_id"]
    print(url)

    # test_get_status
    task_is_not_finished = True
    while task_is_not_finished:
        response = client.get(reverse(viewname="get_status") + f"?task_id={task_id}")
        answer = response.json()["task_id"]
        # assert answer != "PENDING"
        if answer == "SUCCESS":
            break

        time.sleep(2)

    # test_get_configs
    response = client.post(reverse(viewname="get_configs"),
           data={
            "task_id": task_id,
            "data_key": data_key,
        },
        format="json",)
    assert "configs" in response.json()


@pytest.mark.integration
@pytest.mark.longtests
def test_install_by_password(client):
    url = reverse(viewname="install")
    data_key=SymmetricEncryptor.generate_key()
    response = client.post(
        reverse(viewname="install"),
        data={
            "auth": "pass",
            "ip_address": "wireguard-pass.light-search.com",
            "user": "root",
            "password": "test_password_for_pipline_usage",
            "private_key": settings.TEST_PRIVATE_KEY,
            "data_key": data_key
        },
        format="json",
    )
    print(response.json())
    task_id = response.json()["task_id"]
    print(url)

    # test_get_status
    task_is_not_finished = True
    while task_is_not_finished:
        response = client.get(reverse(viewname="get_status") + f"?task_id={task_id}")
        answer = response.json()["task_id"]
        # assert answer != "PENDING"
        if answer == "SUCCESS":
            break

        time.sleep(2)

    # test_get_configs
    response = client.post(reverse(viewname="get_configs"),
        data={
            "task_id": task_id,
            "data_key": data_key,
        },
        format="json",)
    assert "configs" in response.json()
    print(response.json())


@pytest.mark.skip(reason="Purely for manual testing")
def test_read_configs():
    from core.celery import turn_configs_to_dictionary
    import json
    from core.celery import REDIS_RESULT_PASSWORD, REDIS_HOST_RESULT
    import redis

    path = "/tmp/server_installer/10f7e655-4280-470d-bf31-8913e069c82c"
    redis_conn = redis.Redis(
        host=REDIS_HOST_RESULT, password=REDIS_RESULT_PASSWORD, port=6379, db=0
    )

    result = json.dumps(turn_configs_to_dictionary(path))

    redis_conn.set("123", result)

    extracted = redis_conn.get("123")
    print(type(extracted))
    print(extracted)

@pytest.mark.integration
def test_dev_redis_works():
    from core.celery import REDIS_RESULT_PASSWORD, REDIS_HOST_RESULT
    import redis

    redis_conn = redis.Redis(
        host=REDIS_HOST_RESULT, password=REDIS_RESULT_PASSWORD, port=30011, db=0
    )
    redis_conn.set("123", "abc")

    extracted = redis_conn.get("123")
    print(type(extracted))
    print(extracted)


def test_sanitizer():
    assert is_input_verified("root")
    assert is_input_verified("r!rtr")
    assert is_input_verified("root4545")
    assert not is_input_verified(" frgfg")
    assert is_input_verified("test_password_for_pipline_usage")


@pytest.mark.integration
@pytest.mark.skip(reason="Purely for manual testing")
def test_get_stdout(client):
    url = reverse(viewname="install")

    response = client.get(
        reverse(viewname="get_stdout")
        + f"?task_id=d79fcbeb-c1e1-4128-9c44-ade38950377e",
        format="json",
    )
    print(response.json())
    print(url)

import core.measurer as measurer

def test_time_measurer():

    start = measurer.start_time_measuring()

    assert type(start) is str
    time.sleep(0.1)

    total = measurer.get_total_time_measuring(start)
    assert total > 0.1
    print(total)
    print(type(total))


from .views import InstallingData

def test_validating_installing_data():
    serializer = InstallingData(data={"auth": "ssh", "user": "456", "ip_address": "123"})
    # with pytest.raises(rest_framework.exceptions.ValidationError):
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)

def test_validating_installing_data_2():
    serializer = InstallingData(data={'auth': 'ssh', 'user': 'root', 'ip_address': 'wireguard-ssh.light-search.com', 'password': ''})
    # with pytest.raises(rest_framework.exceptions.ValidationError):
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)

def test_check_generating_ssh_key_pair(client):
    url = reverse(viewname="get_ssh_key_pair")

    response = client.get(
        url,
    )
    data = response.json()
    print(url)

    print(data)

