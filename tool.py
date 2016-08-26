from ConfigParser import SafeConfigParser
from os.path import isfile
import logging

logging.basicConfig(level=logging.INFO)

CONFIG_FILE = 'deploy.cfg'
CONFIG_SECTION = 'unik'
RASPBERRY_IP_OPTION = 'raspberry_ip'
REPO_URL_OPTION = 'repository_url'
REPO_NAME_OPTION = 'repository_name'

config = SafeConfigParser()

def prompt_repository():
    url = raw_input('Please input git url for your hub project:')
    config.set(CONFIG_SECTION, REPO_URL_OPTION, url)
    config.set(CONFIG_SECTION, REPO_NAME_OPTION, _get_repository_name(url))


def _get_repository_name(url):
    return url.rsplit('/')[-1].rsplit('.')[0]


def prompt_raspberry_ip():
    ip = raw_input('Please input the ip of you raspberry pi:')
    config.set(CONFIG_SECTION, RASPBERRY_IP_OPTION, ip)


def init_config():
    if not isfile(CONFIG_FILE):
        config.add_section(CONFIG_SECTION)
        prompt_repository()
        prompt_raspberry_ip()
    else:
        with open(CONFIG_FILE) as config_fp:
            config.readfp(config_fp)
    if not config.has_option(CONFIG_SECTION, REPO_URL_OPTION):
        prompt_repository()
    if not config.has_option(CONFIG_SECTION, RASPBERRY_IP_OPTION):
        prompt_raspberry_ip()
    with open(CONFIG_FILE, 'w') as config_fp:
        config.write(config_fp)