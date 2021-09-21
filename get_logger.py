import logging
import os

import graypy
import yaml


def get_logger():
    logger = logging.getLogger('graylog')
    logger.setLevel(logging.INFO)

    if os.path.exists('graylog.yml'):
        graylog_ip = yaml.safe_load(open("graylog.yml", 'r'))['graylog_ip']
        handler = graypy.GELFUDPHandler(graylog_ip, 12201, localname="get_pdf_paragraphs")
        logger.addHandler(handler)
    else:
        os.chmod('./docker_volume', 0o666)
        logger.addHandler(logging.FileHandler('./docker_volume/service.log'))

    return logger
