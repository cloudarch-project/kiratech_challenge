[![Python](https://img.shields.io/pypi/pyversions/azure-cli.svg?maxAge=2592000)](https://pypi.python.org/pypi/azure-cli) ![CI](https://github.com/nickjj/ansible-docker/workflows/CI/badge.svg?branch=master)

## Deploy Centos Based VM on Azure with GitActions pipeline

1. Create a service principal on Azure with the following command : 
    - az ad sp create-for-rbac --name GitActionsPipeline --role Contributor --sdk-auth

        The output is in json format, copy and paste into credential file, will be use later with the pipeline. Output is like this  : 
```
       {
        "clientId": "************************************",
        "clientSecret": "*********************************",
        "subscriptionId": "*********************************",
        "tenantId": "*********************************",
        "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
        "resourceManagerEndpointUrl": "https://management.azure.com/",
        "activeDirectoryGraphResourceId": "https://graph.windows.net/",
        "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
        "galleryEndpointUrl": "https://gallery.azure.com/",
        "managementEndpointUrl": "https://management.core.windows.net/"
        }
```
Add the output in the GitActions Secret as AZURE_CREDENTIALS variable, we'll use later for AZ CLI task to connect to azure.

## Here we find the Code for the Pipeline: 
2. Need to create local env with venv  
    - sudo apt install python3-pip
    - sudo apt install python3.8-venv
    - python3 -m venv ansible-playbook && . ansible-playbook/bin/activate && pip3 install --upgrade

3. Install ansible and Playbook Azure Galaxy
    - pip && pip3 install wheel
    - pip3 install ansible==2.10.0
    - ansible-galaxy collection install azure.azcollection
    - pip3 install -r ~/.ansible/collections/ansible_collections/azure/azcollection/requirements-azure.txt
    - ./ansible-playbook/bin/ansible --version
4. Copy Credentials to GitActions Pipeline's User
    - cp main/ansible/keys/credentials ~/.azure

## Now we have the env ready we can create Centos VM from Azure Ansible Playbook. 
## https://docs.microsoft.com/en-us/azure/developer/ansible/vm-configure?tabs=ansible


5. Install Docker Ansible 
[Docker Ansible Reference Centos](https://docs.ansible.com/ansible/latest/collections/community/docker/docsite/scenario_guide.html#ansible-collections-community-docker-docsite-scenario-guide)

6. Play Ansible Playbook for the Challenge

## Play ansible:

```
ansible-playbook prerequisite.yml -i hosts -b
ansible-playbook partition.yml -i hosts -b
ansible-playbook docker.yml -i hosts -b
```

In the Azure machine we can export the env variable 
export DOCKER_HOST=tcp://10.0.1.4:2375

Or add the env variable permently, create a file under the /etc/profile.d/ folder and add the variable on it

```
sudo vim /etc/profile.d/env.sh
```
