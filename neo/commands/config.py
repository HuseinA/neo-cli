import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.commands import store

class Config(Base):
	"""
usage: 
  config ( ls | create | inspect | rm)

Manage Neo configs

Options:
  --help   Print usage

Commands:
  create      Create a configuration file from a file or STDIN as content
  inspect     Display detailed information on one or more configuration files
  ls          List configs
  rm          Remove one or more configuration files
    """
	def execute(self):
		if self.args['create']:
			print "Config create test"
		if self.args['inspect']:
			print "Config inspect test"
		if self.args['ls']:
			print "Config ls test"
		if self.args['rm']:
			print "Config rm test"

