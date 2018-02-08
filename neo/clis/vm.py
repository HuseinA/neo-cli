import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.clis import store
from neo.libs import vm as vm_lib
import os
import re

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
            data_instance = vm_lib.get_list()
            print(tabulate(data_instance, headers=[
                  "ID", "Name"], tablefmt="grid"))
        if self.args['rm']:
            try:
                if self.args['<id_instance>'] == '-h':
                    subprocess.check_output(['neo vm', '--help'])
                else:
                    instance_id = self.args['<id_instance>']
                    answer = ""
                    while answer not in ["y", "n"]:
                        answer = input(
                            "Are you sure to delete this instance [Y/N]? ").lower()

                    if answer == "y":
                        vm_lib.do_delete(instance_id)
                        print("instance has been deleted")
            except Exception as e:
                print(e)
            else:
                pass
            finally:
                pass
