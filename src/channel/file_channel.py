"""
@copyright: 2018 Data Wizard
"""

from src.channel.channel import Channel
from src.source.filesystem_source import FileSystemSource
from src.destination.s3destination import S3Destination
from distutils.dir_util import copy_tree
import logging
import boto3
import os
import datetime


class FileChannel(Channel):
    """
    Copying From source to destination
    """

    def __init__(self, wait_time, executions):
        super().__init__(wait_time, executions)

    def execute(self, source: FileSystemSource, destination: S3Destination):
        logger = logging.getLogger("universal_ingest")
        if type(destination) is S3Destination:
            s3 = boto3.client('s3')
            response = s3.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            if destination.bucket_name not in buckets:
                s3.create_bucket(Bucket=destination.bucket_name)
            for file in os.listdir(source.directory):
                s3.upload_file(os.path.join(source.directory, file), destination.bucket_name,
                               os.path.join(source.directory, file))
        else:
            copy_tree(source.directory, destination.bucket_name)
            logger.debug("files copied")

        self.last_executed = datetime.datetime.now()
        self.executions = self.executions + 1
