"""
@copyright: 2018 Data Wizard
"""


class Channel:
    """
    Base class for transferring files
    """

    def __init__(self, wait_time, total_executions):
        self.last_executed = None
        self.wait_time = wait_time
        self.total_executions = total_executions
        self.executions = 0

    def execute(self, source, destination):
        """
        Execute
        :param source:
        :param destination:
        :return:
        """
        pass
