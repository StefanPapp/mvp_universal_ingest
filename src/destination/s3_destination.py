"""
@copyright: 2017 Data Wizard
"""

import os

from src.destination.destination import Destination


class S3_Destination(Destination):

    @staticmethod
    def upload_dir(dir, bucket):
        if not os.path.isdir(dir):
            return False


