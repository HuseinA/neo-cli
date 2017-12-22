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
from heatclient.client import Client
from heatclient.common import template_utils
import re

from novaclient import client as nova_client


home = os.path.expanduser("~")
class Vm(Base):
	"""
usage: 
  vm ( ls | rm <id_instance>)

Manage virtual machine

Options:
  --help   Print usage

Commands:
  ls			List of virtual machine
  rm <id_instance>     	Remove one of machine

Run 'neo vm COMMAND --help' for more information on a command.
    """
	def execute(self):
		if self.args['ls']:
		    if not login_lib.check_env():
		    	print 'you are not authorized.'
		    else:
				login_lib.load_env_file()
				heat_url = 'https://heat.wjv-1.neo.id:8004/v1/%s' % os.environ.get("OS_PROJECT_ID")
				heat = Client('1', endpoint=heat_url, token=os.environ.get("OS_TOKEN"))
				instances = [instance for instance in heat.stacks.list()]
				for instance in instances:
				    print " -> ({}) {}".format(instance.id, instance.name)
				    print instance.to_dict()
				if len(instances) == 0:
					print "There is no virtual machine;"
		if self.args['rm'] :
			if not login_lib.check_env():
				print 'you are not authorized.'
			else:
				try:
					if self.args['<id_instance>'] == '-h':
						subprocess.check_output(['neo vm','--help'])
					else:
						login_lib.load_env_file()
						heat_url = 'https://heat.wjv-1.neo.id:8004/v1/%s' % os.environ.get("OS_PROJECT_ID")
						heat = Client('1', endpoint=heat_url, token=os.environ.get("OS_TOKEN"))
						stack_id = self.args['<id_instance>']
						heat.stacks.delete(stack_id)
				except Exception, e:
					print e
				else:
					pass
				finally:
					pass