"""
@copyright: 2018 Data Wizard
"""

import logging


class LogManager:
    """
    LogManager
    """

    def __init__(self):
        logger = logging.getLogger("universal_ingest")
        logger.debug("logger started")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)
