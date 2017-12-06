import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Deploy(Base):
	"""
usage: 
  deploy

Deploy 

Run 'neo deploy COMMAND --help' for more information on a command.
    """
	def execute(self):
		print "Deploy test"
