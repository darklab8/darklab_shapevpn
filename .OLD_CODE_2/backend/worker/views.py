from django.conf import settings

# from main.universal import required_key
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import input_verificator, SanitizationError
from core.celery import task_vpn_install
from django.conf import settings
from celery.result import AsyncResult
from core.celery import redis_conn
import logging
import core.measurer as measurer
from rest_framework import serializers
import json
import time
from core.encryptor import AssymetricEncryptor, secret_encryptor, SymmetricEncryptor
import secrets

# Create your views here.


def get_client_ip(request):
    return request.META


@api_view(["GET", "POST"])
def get_ping(request):
    print(f"meta={request.META}")
    return Response({"message": "pong!"})


@api_view(["POST"])
def ping_with_sleeping(request):

    if request.data["password"] != "34c523523o834v2357o2354734o":
        return Response({"error": "forbidden"}, status=403)

    time.sleep(1)
    return Response({"message": "pong!"})
    
    


@api_view(["POST"])
def check_data(request):
    return Response(request.data)




class InstallingData(serializers.Serializer):
    auth = serializers.CharField(max_length=10)
    ip_address = serializers.CharField(max_length=50)
    user = serializers.CharField(max_length=100)

@api_view(["POST"])
def install_vpn_server(request):

    unique_id = secrets.token_hex(16)
    try:
        ip = get_client_ip(request)
    except Exception as error:
        ip = f"undefined, {str(error)}"

    logging.info(f"unique_id={unique_id}, type=install_vpn_server, msg=start, ip={ip}")

    logging.info(f'unique_id={unique_id}, type=attempting to validate, ip={request.data["ip_address"]}, keys={request.data.keys()}')
    serializer = InstallingData(data=request.data)
    serializer.is_valid(raise_exception=True)

    logging.info(f"unique_id={unique_id}, data is validated")

    logging.info(
        f"unique_id={unique_id}, type=install_vpn_server, msg=processed_input"
    )

    task = task_vpn_install.delay(
        auth=request.data["auth"],
        ip_address=request.data["ip_address"],
        user=request.data["user"],
        password=secret_encryptor.encrypt_str(request.data.get("password", "")),
        server_ssh_port=request.data.get("server_ssh_port", "22"),
        server_vpn_port=request.data.get("server_vpn_port", "31280"),
        start=measurer.start_time_measuring(),
        private_key=secret_encryptor.encrypt_str(request.data["private_key"]),
        data_key=secret_encryptor.encrypt_str(request.data["data_key"]),
        unique_id=unique_id,
    )

    logging.info(
        f"unique_id={unique_id}, type=install_vpn_server, msg=finish, status_code=200, task_id={task.id}, ip={ip}"
    )
    return Response({"task_id": task.id})


@api_view(["GET"])
def get_status(request):

    print(request.query_params)
    task_id = request.query_params["task_id"]

    task = AsyncResult(task_id)

    print(f"meta={task.info}")
    
    try:
        json.dumps(task.info)
        meta = task.info
    except (TypeError, OverflowError):
        meta = {}

    return Response({"task_id": task.status, "meta": meta})


@api_view(["POST"])
def get_configs(request):

    print(request.data)
    task_id = request.data["task_id"]

    encrypted = redis_conn.get(f"{task_id}_configs")
    decryptor = SymmetricEncryptor(request.data["data_key"])

    decrypted = decryptor.decrypt_str(encrypted.decode())

    return Response({"configs": decrypted})


@api_view(["GET"])
def get_stdout(request):

    print(request.query_params)
    task_id = request.query_params["task_id"]

    configs = redis_conn.get(f"{task_id}_stdout")

    return Response({"stdout": configs})


@api_view(["GET"])
def get_ssh_key_pair(request):
    private, public = AssymetricEncryptor.generate_keys()
    data_key = SymmetricEncryptor.generate_key()
    return Response({"private": private, "public": public, "data_key": data_key})

    