import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.clis import store
from neo.libs import login as login_lib
import os
import re

from novaclient import client as nova_client
from tabulate import tabulate


class Vm(Base):
    """
usage: 
vm ( ls | rm <id_instance>)

Manage virtual machine

Options:
--help   Print usage

Commands:
ls			List of virtual machine
rm <id_instance>     	Remove one of machine

Run 'neo vm COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args['ls']:
            compute = nova_client.Client(2, session=login_lib.get_session())
            instances = [instance for instance in compute.servers.list()]
            data_instance = [[instance.id, instance.name]
                             for instance in instances]
            print(tabulate(data_instance, headers=[
                  "ID", "Name"], tablefmt="grid"))
        if self.args['rm']:
            try:
                if self.args['<id_instance>'] == '-h':
                    subprocess.check_output(['neo vm', '--help'])
                else:
                    compute = nova_client.Client(
                        2, session=login_lib.get_session())
                    instance_id = self.args['<id_instance>']
                    answer = ""
                    while answer not in ["y", "n"]:
                        answer = input(
                            "Are you sure to delete this instance [Y/N]? ").lower()

                    if answer == "y":
                        compute.servers.delete(instance_id)
                        print("instance has been deleted")
                    # compute.servers.unlock(instance_id)
                    # compute.servers.resume(instance_id)
            except Exception as e:
                print(e)
            else:
                pass
            finally:
                pass
