#!/usr/bin/env python3
import subprocess

def excute(commands):
    for command in commands:
        status = subprocess.call(command,shell=True)

commands = [
    'sudo apt update',
    'sudo apt remove docker docker-engine docker.io',
    'sudo apt install -y apt-transport-https ca-certificates curl software-properties-common',
    'curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -',
    'sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"',
    'sudo apt update',
    'echo "start install docker..."',
    'sudo apt install -y docker-ce',
    'echo "start install docker compose"',
    'sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
    'sudo chmod +x /usr/local/bin/docker-compose',
    'sudo docker-compose --version',
    'echo "set docker mirrors configuration"',
    'sudo echo \'{"registry-mirrors":["https://registry.docker-cn.com"]}\' > daemon.json',
    'sudo mv daemon.json /etc/docker/',
    'sudo systemctl daemon-reload',
    'sudo usermod -aG docker $USER',
    'sudo service docker restart'
]
print('install docker and docker-compose')
excute(commands)