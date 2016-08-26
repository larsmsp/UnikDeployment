import logging
import tool

from fabric.api import *
from fabric.contrib.files import exists

tool.init_config()
repo_url = tool.config.get(tool.CONFIG_SECTION, tool.REPO_URL_OPTION)
repo_name = tool.config.get(tool.CONFIG_SECTION, tool.REPO_NAME_OPTION)
raspberry_ip = tool.config.get(tool.CONFIG_SECTION, tool.RASPBERRY_IP_OPTION)
logging.info('Repository URL: %s', repo_url)
logging.info('Repository name: %s', repo_name)
logging.info('Raspberry Pi: %s', raspberry_ip)

env.hosts = [raspberry_ip]
env.user = 'pi'
env.password = 'raspberry'


def test():
    run('uname -a')


def clone():
    run('git clone %s' % repo_url)


def commit():
    local('git add -p && git commit')


def push():
    local('git push')


def prepare_deploy():
    commit()
    push()


def pull():
    run('git pull')


def deploy():
    directory = 'home/pi/%s' % repo_name
    if exists(directory):
        with cd(directory):
            pull()
    else:
        clone()