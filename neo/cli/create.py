import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.cli import store
from neo.libs import login as login_lib
import os

class Create(Base):
	"""

usage: create <templates> 

Log in to Neo Cloud
	"""
		
	def execute(self):
		templates = self.args['<templates>']
		from heatclient import client as heat_client
		login_lib.load_env_file()
		libs_dir = os.path.dirname(os.path.realpath(__file__))
		templates_index = "{}/templates/{}/index.yaml".format(libs_dir,templates)
		templates_env = "{}/templates/{}/env.yaml".format(libs_dir,templates)

		heat_url = 'https://heat.wjv-1.neo.id:8004/v1/%s' % os.environ.get("OS_PROJECT_ID")
		heat = heat_client.Client('1', endpoint=heat_url, token=os.environ.get("OS_TOKEN"))
		template = open(templates_index)
		env = open(templates_env)
		heat.stacks.create(stack_name=templates,template=template.read(), environment=env.read())
