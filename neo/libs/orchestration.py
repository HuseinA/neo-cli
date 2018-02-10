from neo.libs import login as login_lib
from neo.libs import utils
from heatclient import client as heat_client
from heatclient.common import template_utils
import os


def get_heat_client():
    login_lib.load_env_file()
    heat_url = 'https://heat.wjv-1.neo.id:8004/v1/%s' % os.environ.get(
        "OS_PROJECT_ID")
    heat = heat_client.Client('1', endpoint=heat_url,
                              token=os.environ.get("OS_TOKEN"))
    return heat


def initialize(manifest_fie):
    init = list()
    utils.log_info("Initialization....")
    key = utils.get_key(manifest_fie)
    for stack in utils.initdir(key):
        for project in key["stack"][stack]:
            template = key["data"][stack][project]["template"]
            parameters = key["data"][stack][project]["parameters"]
            url = utils.repodata()[stack][template]["url"]
            dest = "{}/{}/{}".format(key["deploy_dir"], stack, project)
            utils.log_info("Build {} {} template".format(project, stack))
            utils.template_url(url, dest)
            utils.log_info("[Done]")
            utils.log_info(
                "Create {} {} environment file".format(project, stack))
            utils.yaml_create("{}/env.yml".format(dest),
                              {"parameters": parameters})
            utils.log_info("[Done]")
            stack_init = {}
            stack_init["dir"] = dest
            stack_init["project"] = project
            stack_init["stack"] = stack
            stack_init["env_file"] = "{}/env.yml".format(dest)
            init.append(stack_init)
    utils.yaml_create("{}/deploy.yml".format(key["deploy_dir"]),
                              init)
    return init


def create(initialize):
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
		        heat.stacks.create(stack_name=deploy_name, template=template,
		                           environment=deploy_env_file.read(), files=files)
		except Exception as e:
				print(e)
		else:
		    pass
		finally:
		    pass
