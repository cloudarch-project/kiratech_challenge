# Deploy 2 Centos Based VM on Azure with GitHubAction pipeline

1. Create a service principal on Azure with the following command : 
        az ad sp create-for-rbac --name GitActionsPipeline --role Contributor --sdk-auth

    The output is in json format, copy and paste into credential file, will be use later with the pipeline. Output is like this  : 
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

2. Need to create local env with venv  
          sudo apt install python3-pip
          sudo apt install python3.8-venv
          python3 -m venv ansible-playbook && . ansible-playbook/bin/activate && pip3 install --upgrade

3. Install ansible and Playbook Azure Galaxy
          pip && pip3 install wheel
          pip3 install ansible==2.10.0
          ansible-galaxy collection install azure.azcollection
          pip3 install -r ~/.ansible/collections/ansible_collections/azure/azcollection/requirements-azure.txt
          ./ansible-playbook/bin/ansible --version
4. Copy 
          cp main/ansible/keys/credentials ~/.azure

# Now we have the env ready we can create Centos VM from Azure Ansible Playbook.
# https://docs.microsoft.com/en-us/azure/developer/ansible/vm-configure?tabs=ansible