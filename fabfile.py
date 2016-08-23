import logging
import tool


tool.init_config()
repo_url = tool.config.get(tool.CONFIG_SECTION, tool.REPO_OPTION)
raspberry_ip = tool.config.get(tool.CONFIG_SECTION, tool.RASPBERRY_IP_OPTION)
logging.info('Repository: %s', repo_url)
logging.info('Raspberry Pi: %s', raspberry_ip)

