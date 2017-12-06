import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Volume(Base):
	"""
usage: 
  volume ( create | inspect | ls | prune | rm)

Manage volumes

Options:
      --help   Print usage

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused volumes
  rm          Remove one or more volumes

Run 'neo volume COMMAND --help' for more information on a command.
    """
	def execute(self):
		if self.args['create']:
			print "volume create test"
		if self.args['inspect']:
			print "volume inspect test"
		if self.args['ls']:
			print "volume ls test"
		if self.args['prune']:
			print "network prune test"
		if self.args['rm']:
			print "volume rm test"

