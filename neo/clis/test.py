import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.libs import network as network_lib
from neo.libs import utils
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
            key = utils.get_key("neo.yml")
            print(key["deploy_dir"])
            for i in utils.initdir(key):
                for j in key["stack"][i]:
                    template = key["data"][i][j]["template"]
                    url = utils.repodata()[i][template]["url"]
                    dest = "{}/{}/{}".format(key["deploy_dir"],i,j)
                    print(template)
                    print(url)
                    utils.template_url(url, dest)

            """print(utils.repodata())"""
