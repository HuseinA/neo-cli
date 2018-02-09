from neo.libs import login as login_lib
from novaclient import client as nova_client


def get_nova_client():
    compute = nova_client.Client(2, session=login_lib.get_session())
    return compute


def get_list():
    compute = get_nova_client()
    instances = [instance for instance in compute.servers.list()]
    return instances


def do_delete(instance_id):
    compute = get_nova_client()
    compute.servers.delete(instance_id)
