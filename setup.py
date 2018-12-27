"""
@copyright: 2018 Data Wizard
"""

import os
from setuptools import setup
from udi import __version__


def _read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name="udi",
    version=__version__,
    author="DW",
    author_email="stefan.papp@data-wizard.net",
    description="universal data ingestor",
    keywords="ingest",
    packages=["udi",
              "udi.core",
              "udi.destination",
              "udi.source",
              "udi.channel"],
    long_description=_read('README.md'),
    zip_safe=True,
    license="2018 Data Wizard. All rights reserved.",
    classifiers=[
        "Development Status :: Release"
    ],
    install_requires=[
        'awscli',
        'pykafka',
        'pyyaml',
        'boto3'
    ]
)
