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
from neo.libs import utils
from neo.libs import orchestration as orch
from tabulate import tabulate


class Test(Base):
    """
usage: 
test ( ls )

Manage network

Options:
--help   Print usage

Commands:
ls			List of network

Run 'neo test COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args['ls']:
            deploy_init = orch.initialize("neo.yml")
            orch.do_create(deploy_init)
            # print(
            #     tabulate(
            #         orch.get_list(),
            #         headers=["ID", "Name", "Status", "Created", "Updated"],
            #         tablefmt="grid"))

            #print(orch.get_stack("peler"))
            #print(orch.check_manifest_file())
