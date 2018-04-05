import click
import getpass
import subprocess
import requests
import os
import re
import bitmath
from json import dumps
from .base import Base
from docopt import docopt
from neo.libs import network as network_lib
from neo.libs import vm as vm_lib
from neo.libs import utils, image
from neo.libs import orchestration as orch
from tabulate import tabulate


class Exec(Base):
    """
usage:
        exec [-f PATH] [-a] [-m|-n]

List all stack

Options:
-h --help               Print usage
-f PATH --file=PATH     Set neo manifest file
-a --all                List all Stacks
-m --virtual-machine    List all Virtual Machines
-n --network            List all Networks

Run 'neo exec COMMAND --help' for more information on a command.
"""

    def execute(self):

        if self.args["--network"]:
            # print(utils.terminal_size())

            exit()
