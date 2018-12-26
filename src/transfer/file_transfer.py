"""
@copyright: 2018 Data Wizard
"""

from src.transfer.transfer import Transfer
from src.source.filesystem_source import FileSystemSource
from src.destination.filesystem_destination import FileSystemDestination
from src.destination.s3destination import S3Destination
from distutils.dir_util import copy_tree
import logging
import boto3
import os
import datetime


class FileTransfer(Transfer):
    """
    Copying From source to destination
    """

    def __init__(self, wait_time, executions):
        super().__init__(wait_time, executions)

    def execute(self, source: FileSystemSource, destination: FileSystemDestination):
        if type(destination) is S3Destination:
            s3 = boto3.client('s3')
            response = s3.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            if destination.directory not in buckets:
                s3.create_bucket(Bucket=destination.directory)
            for file in os.listdir(source.directory):
                s3.upload_file(os.path.join(source.directory, file), destination.directory, file)
        else:
            copy_tree(source.directory, destination.directory)
            logger = logging.getLogger("universal_ingest")
            logger.debug("files copied")

        self.last_executed = datetime.datetime.now()
        self.executions = self.executions + 1
