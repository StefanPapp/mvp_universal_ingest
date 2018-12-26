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
        self.threads = []

    def start(self, mappings):
        """
        Starting channel
        :param mappings:
        :return:
        """
        for mapping in mappings:
            self.threads.append(self.executor.submit(WorkFlow.send, mapping))

        # Wait for all tasks to finish
        while self.threads:
            self.threads.pop().result()
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
        while mapping.transfer.total_executions != -1 and \
                mapping.transfer.executions <= mapping.transfer.total_executions:

            if mapping.transfer.last_executed is None or mapping.transfer.last_executed + \
                    mapping.transfer.last_executed + mapping.transfer.wait_time*60 > ts:
                mapping.transfer.execute(mapping.source, mapping.destination)
