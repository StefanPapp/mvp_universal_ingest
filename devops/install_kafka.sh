#!/bin/bash
# java is preinstalled

# using 2.11 scala as still standard in ubuntu 18.10
# mkdir opt
wget https://www-us.apache.org/dist/kafka/2.1.0/kafka_2.11-2.1.0.tgz -P /tmp/
tar -xvf /tmp/kafka_2.11-2.1.0.tgz
mv /kafka_2.11-2.1.0 /opt/kafka

echo -e "\nexport PATH=\$PATH:/opt/kafka/bin" >> /root/.bashrc
echo -e "\nexport PATH=\$PATH:/opt/kafka/bin" >> /root/.zshrc