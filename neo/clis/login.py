import click
import getpass
import subprocess
from json import dumps
from neo.clis.base import Base
from docopt import docopt
from neo.libs import login as login_lib


class Login(Base):
    """
usage: login

Log in to Neo Cloud
	"""

    def execute(self):
        login_lib.do_login()
