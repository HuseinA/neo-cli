import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Delete(Base):
	"""
usage: 
  delete

Manage Delete 

Run 'neo delete COMMAND --help' for more information on a command.
    """
	def execute(self):
		print "delete test"
