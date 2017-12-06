import simplejson as json
from keystoneauth1 import exceptions as ks_exceptions
from keystoneauth1 import session as ks_session
from osc_lib import exceptions
from openstackclient.i18n import _
from .base import Base
from docopt import docopt

class Created(Base):
	"""
usage: 
  created

Log out from Neo Gio Cloud

	"""

	def execute(self):
		print 'test of created module'