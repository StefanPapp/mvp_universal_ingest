"""
@copyright: 2018 Data Wizard
"""

import time
import logging

from concurrent.futures import ThreadPoolExecutor


class WorkFlow:
    """
    Workflow
    """

    def __init__(self, executors):
        self.executor = ThreadPoolExecutor(max_workers=executors)
        self.threadpool_components = []

    def start(self, mappings):
        """
        Starting transfer
        :param mappings:
        :return:
        """
        for mapping in mappings:
            self.threadpool_components.append(self.executor.submit(WorkFlow.send, mapping))

        # Wait for all tasks to finish
        while self.threadpool_components:
            self.threadpool_components.pop().result()
        logger = logging.getLogger("universal_ingest")
        logger.debug("done")

    @staticmethod
    def send(mapping):
        """
        Executing
        :param mapping:
        :return:
        """
        ts = time.time()

        if mapping.transfer.last_executed is None or mapping.transfer.last_executed + \
                mapping.transfer.last_executed + mapping.transfer.wait_time*60 > ts:
            mapping.transfer.execute(mapping.source, mapping.destination)
            mapping.last_executed = ts
