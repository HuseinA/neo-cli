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
from neo.libs import utils, ncurses
from neo.libs import orchestration as orch
from tabulate import tabulate


class Create(Base):
    """
usage: 
        create
        create [-f PATH]
        create [-t TEMPLATE]

List all stack

Options:
-h --help                           Print usage
-f PATH --file=PATH                 Set neo manifest file
-t TEMPLATE --template TEMPLATE     Create neo.yml, TEMPLATE is ENUM(clusters,instances,networks)

Run 'neo create COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args["--template"]:
            if self.args["--template"] in ('clusters', 'instances',
                                           'networks'):
                tmpl = self.args["--template"]
                ncurses.init(stack=tmpl)
            exit()

        headers = ["ID", "Name", "Status", "Created", "Updated"]

        set_file = self.args["--file"]
        default_file = orch.check_manifest_file()

        if set_file:
            if os.path.exists(set_file):
                default_file = set_file
            else:
                utils.log_err("{} file is not exists!".format(set_file))
                exit()

        if not default_file:
            utils.log_err("Can't find neo.yml manifest file!")
            q_stack = utils.question(
                "Do you want to generate neo.yml manifest? ")

            if q_stack:
                ncurses.init()

            exit()

        deploy_init = orch.initialize(default_file)
        try:
            orch.do_create(deploy_init)
        except:
            utils.log_err("Deploying Stack failed...")
            exit()

        projects = utils.get_project(default_file)

        project_list = list()
        for project in projects:
            proj = orch.get_stack(project)
            if proj:
                project_list.append(proj)

        if len(project_list) > 0:
            print(tabulate(project_list, headers=headers, tablefmt="grid"))
