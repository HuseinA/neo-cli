import os
from .base import Base
from neo.libs import network as network_lib
from neo.libs import vm as vm_lib
from neo.libs import utils, image
from neo.libs import orchestration as orch
from tabulate import tabulate


class Exec(Base):
    """
usage:
        exec ssh <USER@HOSTS>
        exec vm <VM_ID>
        exec stack <STACK_NAME>

Remote service for stack controller, virtual machine, or ssh machine

Options:
-k KEY_FILE --key=KEY_FILE            Setup keyfile to ssh service

Commands:
  vm <VM_ID>                          Remote to Virtual Machine
  stack <STACK_NAME>                  Remote to stack controller
  ssh <USER@HOSTS>                    Use ssh to remote machines

Run 'neo exec COMMAND --help' for more information on a command.
"""

    def execute(self):
        if self.args["ssh"]:
            cridential = self.args["<USER@HOSTS>"].split("@")
            if len(cridential) != 2:
                print(self.__doc__)
                exit(0)

            user = cridential[0]
            hostname = cridential[1]
            utils.ssh_shell(hostname, user)
        if self.args["vm"]:
            vm_id = self.args["VM_ID"]
            """
                cek vm metadata from stack
            """
