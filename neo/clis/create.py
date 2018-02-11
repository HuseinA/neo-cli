import click
import getpass
import subprocess
from json import dumps
from .base import Base
from docopt import docopt
import requests
from neo.libs import login as login_lib
import os
from heatclient import client as heat_client
from heatclient.common import template_utils


class Create(Base):
    """

usage: create <templates> 

create in to Neo Cloud
    """

    def execute(self):
        templates = self.args['<templates>']
        try:
            if not login_lib.check_env():
                print('you are not authorized.')
            else:
                login_lib.load_env_file()
                libs_dir = os.path.dirname(os.path.realpath(__file__))
                # os.chdir("{}/templates/{}".format(libs_dir,templates))
                template_file = "{}/templates/{}/index.yaml".format(
                    libs_dir, templates)
                template_env = "{}/templates/{}/env.yaml".format(
                    libs_dir, templates)
                heat_url = 'https://heat.wjv-1.neo.id:8004/v1/%s' % os.environ.get(
                    "OS_PROJECT_ID")

                # template = open(templates_index)
                env = open(template_env)
                files, template = template_utils.process_template_path(
                    template_file)

                heat = heat_client.Client(
                    '1', endpoint=heat_url, token=os.environ.get("OS_TOKEN"))

                heat.stacks.create(
                    stack_name=templates,
                    template=template,
                    environment=env.read(),
                    files=files)
        except Exception as e:
            print(e)
        else:
            pass
        finally:
            pass
