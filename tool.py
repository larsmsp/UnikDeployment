from ConfigParser import SafeConfigParser
from os.path import isfile
import logging

logging.basicConfig(level=logging.INFO)

CONFIG_FILE = 'unik.cfg'
CONFIG_SECTION = 'unik'
RASPBERRY_IP_OPTION = 'raspberry'
REPO_OPTION = 'repository'

config = SafeConfigParser()

def prompt_repository():
    url = raw_input('Please input git url for your hub project:')
    config.set(CONFIG_SECTION, REPO_OPTION, url)


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
    if not config.has_option(CONFIG_SECTION, REPO_OPTION):
        prompt_repository()
    if not config.has_option(CONFIG_SECTION, RASPBERRY_IP_OPTION):
        prompt_raspberry_ip()
    with open(CONFIG_FILE, 'w') as config_fp:
        config.write(config_fp)