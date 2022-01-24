def get_graph_client(subscription_id):
    if "tenantId" in os.environ:
        print('using environment variables')
        config_dict = {
            "clientId": os.environ["c6a0385a-1cd7-4673-a516-22194f97fa23"],
            "clientSecret": os.environ["Tv.XitBa6tvKg.WZu~zgXUIhrEvGo9xA50"],
            "subscriptionId": "e7a84c33-0304-4979-b422-1ea40066fa15",
            "tenantId": os.environ["0634f583-e93e-4a11-9749-058651409f10"],
            "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
            "resourceManagerEndpointUrl": "https://management.azure.com/",
            "activeDirectoryGraphResourceId": "https://graph.windows.net/",
            "managementEndpointUrl": "https://management.core.windows.net/"
        }
        client = get_client_from_json_dict(
            GraphRbacManagementClient, config_dict)
    else:
        print('using CLI credentials')
        credential = AzureCliCredential()
        client = GraphRbacManagementClient(credential, subscription_id)
    return client
