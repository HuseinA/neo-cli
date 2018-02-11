from neo.libs import login as login_lib
from neo.libs import utils
from heatclient import client as heat_client
from heatclient.common import template_utils
import os
import time


def get_heat_client():
    try:
        heat = heat_client.Client('1', session=login_lib.get_session())
        return heat
    except Exception as e:
        print(e)


def initialize(manifest_fie):
    init = list()
    utils.log_info("Initialization....")
    key = utils.do_deploy_dir(manifest_fie)
    for stack in utils.initdir(key):
        for project in key["stack"][stack]:
            template = key["data"][stack][project]["template"]
            parameters = key["data"][stack][project]["parameters"]
            url = False

            try:
                url = utils.repodata()[stack][template]["url"]
            except:
                utils.log_err("template {} is not exist!".format(template))
                exit()

            dest = "{}/{}/{}".format(key["deploy_dir"], stack, project)
            utils.log_info("Build {} {} template".format(project, stack))

            if not utils.template_url(url, dest):
                utils.log_err("Check your internet connection!")
                exit()

            utils.log_info("Done...")
            utils.log_info("Create {} {} environment file".format(
                project, stack))
            utils.yaml_create("{}/env.yml".format(dest), {
                "parameters": parameters
            })
            utils.log_info("Done...")
            stack_init = {}
            stack_init["dir"] = dest
            stack_init["project"] = project
            stack_init["stack"] = stack
            stack_init["env_file"] = "{}/env.yml".format(dest)
            init.append(stack_init)
    utils.yaml_create("{}/deploy.yml".format(key["deploy_dir"]), init)
    return init


def check_manifest_file():
    neo_file = None
    cwd = os.getcwd()
    if os.path.exists("{}/neo.yaml".format(cwd)):
        neo_file = "{}/neo.yaml".format(cwd)
    if os.path.exists("{}/neo.yml".format(cwd)):
        neo_file = "{}/neo.yml".format(cwd)
    return neo_file


def do_create(initialize):
    try:
        heat = get_heat_client()
        for deploy in initialize:
            deploy_init_file = "{}/init.yml".format(deploy["dir"])
            deploy_file = utils.yaml_parser(deploy_init_file)["create"]
            """ template """
            deploy_template = "{}/{}".format(deploy["dir"], deploy_file)
            deploy_env_file = open(deploy["env_file"])
            deploy_name = deploy["project"]
            files, template = template_utils.process_template_path(
                deploy_template)
            heat.stacks.create(
                stack_name=deploy_name,
                template=template,
                environment=deploy_env_file.read(),
                files=files)

            if deploy["stack"] == "clusters":
                utils.log_info("Generate {} private key...".format(
                    deploy["project"]))
                wait_key = True
                while wait_key:
                    out = get_private_key(
                        deploy["project"])["output"]["output_value"]
                    if out:
                        private_key_file = "{}/private_key.pem".format(
                            deploy["dir"])
                        with open(private_key_file, "w") as pkey:
                            pkey.write(out)
                            os.chmod(private_key_file, 600)
                            utils.log_info("Done...")
                        wait_key = False
                    else:
                        time.sleep(5)

    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass


def get_list():
    heat = get_heat_client()
    stacks = heat.stacks.list()
    data_stack = [[
        stack.id, stack.stack_name, stack.stack_status_reason,
        stack.creation_time, stack.updated_time
    ] for stack in stacks]
    return data_stack


def get_stack(stack_name):
    heat = get_heat_client()
    data_stack = None
    try:
        stack = heat.stacks.get(stack_name)
        data_stack = [
            stack.id, stack.stack_name, stack.stack_status_reason,
            stack.creation_time, stack.updated_time
        ]
    except:
        pass
    return data_stack


def get_private_key(stack_name):
    heat = get_heat_client()
    private_key = None
    try:
        private_key = heat.stacks.output_show(stack_name, "private_key")
    except:
        pass

    return private_key


def do_delete(stack_name):
    heat = get_heat_client()
    try:
        heat.stacks.delete(stack_name)
        return True
    except:
        pass

    return False