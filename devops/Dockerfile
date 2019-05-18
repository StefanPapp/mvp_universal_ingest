FROM stefanpapp/devenv:latest
LABEL Maintainer="Stefan Papp stefan.papp@data-wizard.net"
RUN pip3 install awscli pykafka dependency_injector boto3
ADD udi-0.0.1-py3-none-any.whl /tmp/udi-0.0.1-py3-none-any.whl
RUN pip3 install /tmp/udi-0.0.1-py3-none-any.whl

