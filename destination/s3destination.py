"""
@copyright: 2018 Data Wizard
"""


from destination.destination import Destination


class S3Destination(Destination):
    """
    This class is responsible for storing data into S3
    """

    def __init__(self, bucket_name):
        super().__init__()
        self._bucket_name = bucket_name

    @property
    def bucket_name(self):
        """

        :return:
        """
        return self._bucket_name

    def validate(self):
        raise NotImplementedError
