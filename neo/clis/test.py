import click
import getpass
import subprocess
import requests
import os
import re
from json import dumps
from .base import Base
from docopt import docopt
from neo.libs import network as network_lib
from neo.libs import utils, image
from neo.libs import vm as vm_test
from tabulate import tabulate


def get_flavor():
    utils.log_info("Get flavors data...")
    flavor_file = "/tmp/.flavor.yml"
    if os.path.exists(flavor_file):
        flavors = utils.yaml_parser(flavor_file)["data"]
    else:
        flavors = list(
            reversed(
                sorted(
                    [flavor.name for flavor in list(vm_test.get_flavor())])))
        utils.yaml_create(flavor_file, {"data": flavors})
    return flavors


def get_img():
    utils.log_info("Get images data...")
    img_file = "/tmp/.images.yml"
    if os.path.exists(img_file):
        imgs = utils.yaml_parser(img_file)["data"]
    else:
        imgs = list(reversed([img.name for img in list(image.get_list())]))
        utils.yaml_create(img_file, {"data": imgs})
    return imgs


class Test(Base):
    """
usage: 
test ( ls )

Manage network

Options:
--help   Print usage

Commands:
ls			List of network

Run 'neo test COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args['ls']:
            flavors = get_flavor()
            images = get_img()
            fields = [
                {
                    "type": "TitleText",
                    "name": "Name",
                    "key": "name"
                },
                {
                    "type": "TitleSelectOne",
                    "name": "Flavors",
                    "key": "role",
                    "values": flavors,
                    "max_height": 7,
                    "value": [
                        0,
                    ]
                },
                {
                    "type": "TitleSelectOne",
                    "name": "Images",
                    "key": "img",
                    "scroll_exit": True,
                    "values": images,
                    "max_height": 7,
                    "value": [
                        0,
                    ]
                },
            ]
            form = utils.form_generator("Form Instalasi", fields)
            if form["role"].value[0]:
                print(flavors[form["role"].value[0]])
            print(form["name"].value)

            # for img in vm_test.get_flavor():
            #     print(img.name)

            # deploy_init = orch.initialize("neo.yml")
            # orch.do_create(deploy_init)
            # print(
            #     tabulate(
            #         orch.get_list(),
            #         headers=["ID", "Name", "Status", "Created", "Updated"],
            #         tablefmt="grid"))

            #print(orch.get_stack("peler"))
            #print(orch.check_manifest_file())
