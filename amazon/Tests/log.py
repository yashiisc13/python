import logging


def logs():
    logger = logging.getLogger('selenium')

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('logfile.log')
    logger.addHandler(handler)
