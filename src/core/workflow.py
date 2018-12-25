
import time
from concurrent.futures import ThreadPoolExecutor


class WorkFlow():
    """
    Workflow
    """

    def __init__(self, executors, sources, destinations, transfers):
        self.executor = ThreadPoolExecutor(max_workers=executors)
        self.threadpool_components = []
        self.sources = sources
        self.destinations = destinations
        self.transfers = transfers

    def start(self, mappings):
        """

        :param mappings:
        :return:
        """
        for mapping in mappings:
            self.threadpool_components.append(self.executor.submit
                                 (self.send, mapping))

        # Wait for all tasks to finish
        while self.threadpool_components:
            self.threadpool_components.pop().result()

    def send(self, mapping):
        ts = time.time()
        if mapping.last_executed is None or mapping.last_executed + mapping.wait_time*60 > ts:
            mapping.transport

            mapping.last_executed = ts
        pass