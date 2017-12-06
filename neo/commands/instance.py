import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Instance(Base):
	"""
usage: 
  instance ( ls | create)

Manage Instance

Options:
  ls 		Show the list
  create 	Create new instance
	"""
	def execute(self):
		if self.args['ls']:
			print "ls instance test"
		if self.args['create']:
			print "Create instance test"

