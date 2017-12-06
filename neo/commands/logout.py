import click
import getpass
import subprocess

from json import dumps

from .base import Base

from docopt import docopt

class Logout(Base):
	"""
usage: 
  logout

Log out from Neo Gio Cloud

	"""
	def execute(self):
		try:
			from keystoneauth1.identity import v3
			from keystoneauth1 import session, plugin
			from keystoneclient.v3 import client
			from novaclient import client as nova_client

			print "Login with your NEO Cloud account"

			username =raw_input("usename: ")
			password = getpass.getpass("password: ")
			auth = v3.Password(auth_url='https://keystone.biznetgio.net:5000/v3',
			                    username=str(username),
			                    password=password,
			                    user_domain_name='biznetgio.net')
			sess = session.Session(auth=auth)
			keystone = client.Client(session=sess)
			project_list = [t.id for t in keystone.projects.list(user=sess.get_user_id())]
			project_default = project_list[0]
			# set_project = client.Client(session=sess,project_id=project_default)
			auth2 = v3.Password(auth_url='https://keystone.biznetgio.net:5000/v3',
			                    username=str(username),
			                    password=str(password),
			                    user_domain_name='biznetgio.net',
			                    project_id=project_default)
			sess2 = session.Session(auth=auth2)

			#print plugin.BaseAuthPlugin().get_project_id(session=sess2);

			compute = nova_client.Client(2, session=sess2)
			#
			instances = [instance for instance in compute.servers.list()]
			print "Login Succeeded".format(instances)
			pass
		except Exception, e:
			print "Login Failed"
		else:
			pass
		finally:
			pass