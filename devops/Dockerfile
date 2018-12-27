FROM stefanpapp/devenv:latest
LABEL Maintainer="Stefan Papp stefan.papp@data-wizard.net"
RUN pip3 install awscli pykafka dependency_injector boto3

ADD install_kafka.sh /tmp/install_kafka.sh
RUN chmod a+x /tmp/install_kafka.sh &&  /tmp/install_kafka.sh

