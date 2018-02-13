import git
import os
import yaml
import codecs
import shutil
import paramiko
import select
import coloredlogs, logging


def do_deploy_dir(manifest_file):
    try:
        manifest = {}
        manifest_dir = os.path.dirname(os.path.realpath(manifest_file))
        manifest["deploy_dir"] = "{}/.deploy".format(manifest_dir)

        if not os.path.isdir(manifest["deploy_dir"]):
            os.makedirs(manifest["deploy_dir"])

        key = get_key(manifest_file)
        manifest["stack"] = key["stack"]
        manifest["data"] = key["data"]

        return manifest

    except Exception as e:
        raise


def get_key(manifest_file):
    try:
        manifest = {
            "stack": {
                "services": [],
                "networks": [],
                "deployments": [],
                "clusters": []
            }
        }

        neo_templates = codecs.open(
            manifest_file, encoding='utf-8', errors='strict')
        manifest["data"] = yaml.load(neo_templates.read())
        for (key, value) in manifest["data"].items():
            manifest["stack"][key] = [i for i, v in value.items()]
        return manifest

    except Exception as e:
        raise


def get_project(manifest_file):
    key = get_key(manifest_file)
    manifest = list()
    manifest += [service for service in key["stack"]["services"]]
    manifest += [network for network in key["stack"]["networks"]]
    manifest += [deploy for deploy in key["stack"]["deployments"]]
    manifest += [cluster for cluster in key["stack"]["clusters"]]

    return manifest


def template_git(url, dir):
    try:
        chk_repo = os.path.isdir(dir)
        if chk_repo:
            shutil.rmtree(dir)

        git.Repo.clone_from(url, dir)
        real_url = os.path.dirname(os.path.realpath(dir))

        return True

    except Exception as e:
        return False


def template_url(url, dest):
    url_split = url.split("+")
    url_type = url_split[0]
    url_val = url_split[1]
    return {'git': template_git(url_val, dest), 'local': url_val}[url_type]


def mkdir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def initdir(manifest):
    active_catalog = list()
    for (k, v) in manifest["stack"].items():
        stack_key = manifest["stack"][k]
        if len(stack_key) > 0:
            mkdir("{}/{}".format(manifest["deploy_dir"], k))
            active_catalog.append(k)
    return active_catalog


def repodata():
    abs_path = os.path.dirname(os.path.realpath(__file__))
    repo_file = "{}/templates/repo.yml".format(abs_path)
    return yaml_parser(repo_file)


def yaml_parser(file):
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream)
            return data

        except yaml.YAMLError as exc:
            print(exc)


def yaml_create(out_file, data):
    with open(out_file, 'w') as outfile:
        try:
            yaml.dump(data, outfile, default_flow_style=False)
            return True

        except yaml.YAMLError as exc:
            print(exc)


def log_info(stdin):
    coloredlogs.install()
    logging.info(stdin)


def log_warn(stdin):
    coloredlogs.install()
    logging.warn(stdin)


def log_err(stdin):
    coloredlogs.install()
    logging.error(stdin)


def ssh_out(hostname, user, key_file, command):
    key = paramiko.RSAKey.from_private_key_file(key_file)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=user, pkey=key)
    log_info("Connected...")
    # Example : "tailf -n 50 /tmp/deploy.log"
    commands = command
    channel = client.get_transport().open_session()
    channel.exec_command(commands)
    while True:
        if channel.exit_status_ready():
            break
        rl, wl, xl = select.select([channel], [], [], 0.0)
        if len(rl) > 0:
            print(channel.recv(1028).decode("utf-8"))
