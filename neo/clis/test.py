import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.libs import network as network_lib
from neo.libs import utils

from neo.libs import orchestration as orch
import os
import re

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
                #orch.create(deploy_init)
