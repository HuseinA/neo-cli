import os
import time
from .base import Base
from neo.libs import network as network_lib
from neo.libs import vm as vm_lib
from neo.libs import utils, image
from neo.libs import orchestration as orch
from tabulate import tabulate


class Exec(Base):
    """
usage:
        exec [-f PATH]
        exec ssh <USER@HOSTS>
        exec vm <VM_ID>
        exec stack <STACK_NAME>

Remote service for stack controller, virtual machine, or ssh machine

Options:
-h --help                             Print usage
-f PATH --file=PATH                   Set neo manifest file
-k KEY_FILE --key=KEY_FILE            Setup keyfile to ssh service

Commands:
  vm <VM_ID>                          Remote to Virtual Machine
  stack <STACK_NAME>                  Remote to stack controller
  ssh <USER@HOSTS>                    Use ssh to remote machines

Run 'neo exec COMMAND --help' for more information on a command.
"""

    def execute(self):
        """
            Remote client over SSH
        """
        if self.args["ssh"]:
            cridential = self.args["<USER@HOSTS>"].split("@")
            if len(cridential) != 2:
                print(self.__doc__)
                exit(0)

            user = cridential[0]
            hostname = cridential[1]
            utils.ssh_shell(hostname, user)
            exit(0)

        """
            Remote VM over SSH
        """
        if self.args["vm"]:
            vm_id = self.args["VM_ID"]
            """
                cek vm metadata from stack
            """
            print(vm_id)
            exit(0)

        """
            Remote by manifest file neo.yaml
        """
        set_file = self.args["--file"]
        default_file = orch.check_manifest_file()
        deploy_file = ".deploy/deploy.yml"

        if set_file:
            if os.path.exists(set_file):
                default_file = set_file
            else:
                utils.log_err("{} file is not exists!".format(set_file))
                exit()

        if not default_file:
            utils.log_err("Can't find neo.yml manifest file!")
            exit()

        if os.path.exists(deploy_file):
            deploy_init = utils.yaml_parser(deploy_file)
            deploy_init = [d_init for d_init in deploy_init if d_init["stack"] in ["instances","clusters","databases"]]
        else:
            deploy_init = orch.initialize(default_file)
            deploy_init = [d_init for d_init in deploy_init if d_init["stack"] in ["instances","clusters","databases"]]

        meta = None
        if len(deploy_init) == 1:
            meta = deploy_init[0]

        if len(deploy_init) > 1:
            meta_project = [pra_meta["project"] for pra_meta in deploy_init]
            meta_field = [{"type": "TitleSelectOne", "name": "Select Project", "key": "project", "values": meta_project}]
            meta_field = utils.prompt_generator("Select project...",meta_field)
            meta = [pra_meta for pra_meta in deploy_init if pra_meta in [meta_field["project"]]][0]

        if meta:
            project_name = meta["project"]
            project_dir = meta["dir"]
            private_key_file = "{}/private_key.pem".format(project_dir)
            project_hostname = None
            project_user = None

            if not os.path.exists(private_key_file):
                utils.log_info("Generate {} private key...".format(
                    project_name))
                wait_key = True
                while wait_key:
                    out = orch.get_private_key(project_name)
                    if out:
                        with open(private_key_file, "w") as pkey:
                            pkey.write(out)
                            os.chmod(private_key_file, 0o600)
                            utils.log_info("Done...")
                        wait_key = False
                    else:
                        time.sleep(5)

            if os.path.exists(private_key_file):
                if not project_hostname:
                    project_hostname = orch.get_metadata(project_name,"controller")
                    project_user = orch.get_metadata(project_name,"user")

                do_ssh = True
                while do_ssh:
                    try:
                        utils.ssh_shell(project_hostname, project_user, key_file=private_key_file)
                        do_ssh = False
                    except:
                        quetion = utils.question("Try again? ")
                        if not quetion:
                            do_ssh = False
                        pass
