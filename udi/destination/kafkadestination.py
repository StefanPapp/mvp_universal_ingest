"""
@copyright: 2018 Data Wizard
"""


from destination.destination import Destination


class KafkaDestination(Destination):
    """
    This class is responsible for storing data into Kafka
    """

    def __init__(self, topic):
        super().__init__()
        self._topic = topic

    @property
    def topic(self):
        """

        :return:
        """
        return self._topic

    def validate(self):
        raise NotImplementedError
