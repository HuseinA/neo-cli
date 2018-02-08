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

from neutronclient.v2_0 import client as neutron_client
from tabulate import tabulate


class Network(Base):
    """
usage: 
network ( ls | rm <id_network>)

Manage network

Options:
--help   Print usage

Commands:
ls			List of network
rm <id_network>     	Remove one of network

Run 'neo network COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args['ls']:
            neutron = neutron_client.Client(session=login_lib.get_session())
            networks = neutron.list_networks()
            data_network = [[network['id'], network['name']]
                             for network in networks['networks']]
            print(data_network)
            print(tabulate(data_network, headers=[
                  "ID", "Name"], tablefmt="grid"))
        if self.args['rm']:
            try:
                if self.args['<id_network>'] == '-h':
                    subprocess.check_output(['neo network', '--help'])
                else:
                    neutron = neutron_client.Client(
                        session=login_lib.get_session())
                    network_id = self.args['<id_network>']
                    answer = ""
                    while answer not in ["y", "n"]:
                        answer = input(
                            "Are you sure to delete this network [Y/N]? ").lower()

                    if answer == "y":
                        neutron.delete_network(network_id)
                        print("network has been deleted")
            except Exception as e:
                print(e)
            else:
                pass
            finally:
                pass
