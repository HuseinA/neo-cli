import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.libs import network as network_lib
import os
import re

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
            data_network = [[network['id'], network['name'], network['status']]
                            for network in network_lib.get_list()]
            print(tabulate(data_network, headers=[
                  "ID", "Name", "Status"], tablefmt="grid"))
        if self.args['rm']:
            try:
                if self.args['<id_network>'] == '-h':
                    subprocess.check_output(['neo network', '--help'])
                else:
                    network_id = self.args['<id_network>']
                    answer = ""
                    while answer not in ["y", "n"]:
                        answer = input(
                            "Are you sure to delete this network [Y/N]? "
                        ).lower()

                    if answer == "y":
                        network_lib.do_delete(network_id)
                        print("network has been deleted")
            except Exception as e:
                print(e)
            else:
                pass
            finally:
                pass
