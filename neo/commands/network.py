import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Network(Base):
	"""
usage: 
  network ( connect | create | disconnect | inspect | ls | prune | rm)

Manage networks

Options:
  --help   Print usage

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'neo network COMMAND --help' for more information on a command.
    """
	def execute(self):
		if self.args['connect']:
			print "network connect test"
		if self.args['create']:
			print "network create test"
		if self.args['disconnect']:
			print "network disconnect test"
		if self.args['inspect']:
			print "network inspect test"
		if self.args['ls']:
			print "network ls test"
		if self.args['prune']:
			print "network prune test"
		if self.args['rm']:
			print "network rm test"

