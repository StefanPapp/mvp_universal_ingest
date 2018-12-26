"""
@copyright: 2018 Data Wizard
"""


import dependency_injector.containers as containers
import dependency_injector.providers as providers

from src.source.filesystem_source import FileSystemSource
from src.destination.filesystem_destination import FileSystemDestination
from src.destination.s3destination import S3Destination
from src.destination.kafkadestination import KafkaDestination
from src.transfer.file_transfer import FileTransfer
from src.transfer.kafka_transfer import KafkaTransfer


class ObjectFactory(containers.DeclarativeContainer):
    """
    A class that serves as a ObjectDictionary
    """

    filesystem_source = providers.Factory(FileSystemSource)
    filesystem_destination = providers.Factory(FileSystemDestination)
    s3 = providers.Factory(S3Destination)
    kafka = providers.Factory(KafkaDestination)
    filesystem_filetransfer = providers.Factory(FileTransfer)
    kafka_filetransfer = providers.Factory(KafkaTransfer)
