# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps

helps['acs'] = """
     type: group
     short-summary: Manage Azure Container Services.
"""
helps['acs dcos'] = """
    type: group
    short-summary: Manage a DC/OS orchestrated Azure Container Service.
"""
helps['acs kubernetes'] = """
    type: group
    short-summary: Manage a Kubernetes orchestrated Azure Container Service.
"""
helps['acs kubernetes get-credentials'] = """
    type: command
    short-summary: Download and install credentials to access a cluster.
"""
helps['acs scale'] = """
    type: command
    short-summary: Change the private agent count of a container service.
"""
helps['acs install-cli'] = """
    type: command
    short-summary: Download and install the DC/OS and Kubernetes command line for a cluster.
"""
helps['acs create'] = """
    type: command
    short-summary: Create a new Azure Container Service cluster.
    examples:
        - name: Create a default acs cluster.
          text: az acs create -g MyResourceGroup -n MyContainerService
        - name: Create a Kubernetes cluster.
          text: az acs create --orchestrator-type Kubernetes -g MyResourceGroup -n MyContainerService
        - name: Create a Kubernetes cluster with a an existing SSH key.
          text: az acs create --orchestrator-type Kubernetes -g MyResourceGroup -n MyContainerService --ssh-key-value /path/to/publickey
        - name: Create an ACS cluster with two agent pools.
          text: az acs create -g MyResourceGroup -n MyContainerService --agent-profiles "[{'name':'agentpool1'},{'name':'agentpool2'}]"
        - name: Create an ACS cluster where the second agent pool has a vmSize specified.
          text: az acs create -g MyResourceGroup -n MyContainerService --agent-profiles "[{'name':'agentpool1'},{'name':'agentpool2','vmSize':'Standard_D2'}]"
        - name: Create an ACS cluster with agent-profiles specified from a file.
          text: az acs create -g MyResourceGroup -n MyContainerService --agent-profiles MyAgentProfiles.json
"""
