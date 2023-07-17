from . import views
from django.urls import path

urlpatterns = [
    # ex: /polls/5/
    path("/ping", views.get_ping, name="ping"),
    path("/ping_with_sleeping", views.ping_with_sleeping, name="ping_with_sleeping"),
    path("/check_data", views.check_data, name="check_data"),
    path("/install", views.install_vpn_server, name="install"),
    path("/status", views.get_status, name="get_status"),
    path("/configs", views.get_configs, name="get_configs"),
    path("/stdout", views.get_stdout, name="get_stdout"),
    path("/get_ssh_key_pair", views.get_ssh_key_pair, name="get_ssh_key_pair"),
]
