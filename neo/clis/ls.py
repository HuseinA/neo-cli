import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.clis import store
from neo.libs import login as login_lib
import os

class Ls(Base):
	"""

usage: ls <templates> 

Log in to Neo Cloud
	"""
	
	def execute(self):
		