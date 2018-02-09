import git
import os
import yaml


def template_url(url, name_template)
    url_split = url.split("+")
    url_type = url_split[0]
    url_val = url_split[1]
    return {
        'git': git_clone(url, ".deploy/{}".format(name_template)),
        'local': url_val
    }[url_type]


def git_clone(url, dir):
    try:
        chk_repo = os.path.isdir(dir)
        if not chk_repo:
            os.makedirs(dir)

        git.Repo.clone_from(url, dir)
        real_url = os.path.dirname(os.path.realpath(dir))

        return True

    except git.exc.GitError as e:
        print(e)
        return False


def yaml(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.load(stream)

        except yaml.YAMLError as e:
            print(e)
