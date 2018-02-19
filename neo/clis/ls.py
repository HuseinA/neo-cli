import click
import getpass
import subprocess
import requests
import os
import re
from json import dumps
from .base import Base
from docopt import docopt
from neo.libs import network as network_lib
from neo.libs import vm as vm_lib
from neo.libs import utils
from neo.libs import orchestration as orch
from tabulate import tabulate


class Ls(Base):
    """
usage: 
        ls [-f PATH] [-a] [-m|-n]

List all stack

Options:
-h --help               Print usage
-f PATH --file=PATH     Set neo manifest file
-a --all                List all Stacks
-m --virtual-machine    List all Virtual Machines
-n --network            List all Networks

Run 'neo ls COMMAND --help' for more information on a command.
"""

    def execute(self):
        headers = ["ID", "Name", "Status", "Created", "Updated"]
        if self.args["--all"]:
            print(tabulate(orch.get_list(), headers=headers, tablefmt="grid"))
            exit()

        set_file = self.args["--file"]
        default_file = orch.check_manifest_file()

        if self.args["--virtual-machine"]:
            data_instance = [[instance.id, instance.name, instance.status]
                             for instance in vm_lib.get_list()]
            print(
                tabulate(
                    data_instance,
                    headers=["ID", "Name", "Status"],
                    tablefmt="grid"))
            exit()

        if self.args["--network"]:
            data_network = [[
                network['id'], network['name'], network['status']
            ] for network in network_lib.get_list()]
            print(
                tabulate(
                    data_network,
                    headers=["ID", "Name", "Status"],
                    tablefmt="grid"))
            exit()

        if set_file:
            if os.path.exists(set_file):
                default_file = "{}".format(set_file)
            else:
                utils.log_err("{} file is not exists!".format(set_file))
                exit()

        if not default_file:
            utils.log_err("Can't find neo.yml manifest file!")
            exit()

        projects = utils.get_project(default_file)

        project_list = list()
        for project in projects:
            proj = orch.get_stack(project)
            if proj:
                project_list.append(proj)

        if len(project_list) > 0:
            print(tabulate(project_list, headers=headers, tablefmt="grid"))
        else:
            utils.log_warn("No Data...")
