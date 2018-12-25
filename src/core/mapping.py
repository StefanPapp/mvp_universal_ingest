"""
@copyright: 2018 Data Wizard
"""


class Mapping:
    """
    Maps Source, Destination and Transport
    """
    def __init__(self, name, source, destination, transport, schedule, executions):
        self.name = name
        self.source = source
        self.destination = destination
        self.transport = transport
        self.wait_time = schedule # schedule for now x min wait until next start
        self.last_executed = None
        self.executions = executions

