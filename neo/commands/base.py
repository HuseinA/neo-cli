from docopt import docopt

import simplejson as json

from keystoneauth1 import exceptions as ks_exceptions
from keystoneauth1 import session as ks_session
from osc_lib import exceptions

from openstackclient.i18n import _

class KeystoneSession(object):
    """Wrapper for the Keystone Session
    Restore some requests.session.Session compatibility;
    keystoneauth1.session.Session.request() has the method and url
    arguments swapped from the rest of the requests-using world.
    """

    def __init__(
        self,
        session=None,
        endpoint=None,
        **kwargs
    ):
        """Base object that contains some common API objects and methods
        :param Session session:
            The default session to be used for making the HTTP API calls.
        :param string endpoint:
            The URL from the Service Catalog to be used as the base for API
            requests on this API.
        """

        super(KeystoneSession, self).__init__()

        # a requests.Session-style interface
        self.session = session
        self.endpoint = endpoint

    def execute(self, method, url, session=None, **kwargs):
        """Perform call into session
        All API calls are funneled through this method to provide a common
        place to finalize the passed URL and other things.
        :param string method:
            The HTTP method name, i.e. ``GET``, ``PUT``, etc
        :param string url:
            The API-specific portion of the URL path
        :param Session session:
            HTTP client session
        :param kwargs:
            keyword arguments passed to requests.request().
        :return: the requests.Response object
        """

        if not session:
            session = self.session
        if not session:
            session = ks_session.Session()

        if self.endpoint:
            if url:
                url = '/'.join([self.endpoint.rstrip('/'), url.lstrip('/')])
            else:
                url = self.endpoint.rstrip('/')

        # Why is ksc session backwards???
        return session.request(url, method, **kwargs)

class BaseAPI(KeystoneSession):
    """Base API"""

    def __init__(
        self,
        session=None,
        service_type=None,
        endpoint=None,
        **kwargs
    ):
        """Base object that contains some common API objects and methods
        :param Session session:
            The default session to be used for making the HTTP API calls.
        :param string service_type:
            API name, i.e. ``identity`` or ``compute``
        :param string endpoint:
            The URL from the Service Catalog to be used as the base for API
            requests on this API.
        """

        super(BaseAPI, self).__init__(session=session, endpoint=endpoint)

        self.service_type = service_type

class Base(object):
    """Base class for the commands"""

    def __init__(self, options,*command_args):
        """
        Initialize the commands.

        :param command_args: arguments of the command
        """
        self.options = options
        self.args = docopt(self.__doc__, command_args)
    def execute(self):
        """Execute the commands"""
        print 'test'
        raise NotImplementedError