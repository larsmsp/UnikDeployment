from ConfigParser import SafeConfigParser
from os.path import isfile
import logging

logging.basicConfig(level=logging.INFO)

CONFIG_FILE = 'deploy.cfg'

GIT_CONFIG_SECTION = 'git'
GIT_PATH_OPTION = 'path'

RASPBERRY_CONFIG_SECTION = 'raspberry'
RASPBERRY_IP_OPTION = 'ip'

REPO_CONFIG_SECTION = 'repository'
REPO_URL_OPTION = 'url'
REPO_NAME_OPTION = 'name'

config = SafeConfigParser()


def prompt_git():
    path = raw_input('Please input the path of your git executable:')
    config.set(GIT_CONFIG_SECTION, GIT_PATH_OPTION, path)


def prompt_repository():
    url = raw_input('Please input git url for your hub project:')
    config.set(REPO_CONFIG_SECTION, REPO_URL_OPTION, url)
    config.set(REPO_CONFIG_SECTION, REPO_NAME_OPTION, _get_repository_name(url))


def _get_repository_name(url):
    return url.rsplit('/')[-1].rsplit('.')[0]


def prompt_raspberry_ip():
    ip = raw_input('Please input the ip of you raspberry pi:')
    config.set(RASPBERRY_CONFIG_SECTION, RASPBERRY_IP_OPTION, ip)


def init_config():
    if not isfile(CONFIG_FILE):
        config.add_section(GIT_CONFIG_SECTION)
        config.add_section(REPO_CONFIG_SECTION)
        config.add_section(RASPBERRY_CONFIG_SECTION)
        prompt_repository()
        prompt_raspberry_ip()
    else:
        with open(CONFIG_FILE) as config_fp:
            config.readfp(config_fp)
    if not config.has_option(GIT_CONFIG_SECTION, GIT_PATH_OPTION):
        prompt_git()
    if not config.has_option(REPO_CONFIG_SECTION, REPO_URL_OPTION):
        prompt_repository()
    if not config.has_option(RASPBERRY_CONFIG_SECTION, RASPBERRY_IP_OPTION):
        prompt_raspberry_ip()
    with open(CONFIG_FILE, 'w') as config_fp:
        config.write(config_fp)