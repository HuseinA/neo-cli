import click
import getpass
import subprocess
from json import dumps
from neo.clis.base import Base
from docopt import docopt
from neo.libs import login as login_lib


class Logout(Base):
    """
usage: login

Log out from Neo Cloud
	"""

    def execute(self):
        login_lib.do_logout()
