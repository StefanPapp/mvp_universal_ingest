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
