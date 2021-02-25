from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'novahub'
    account_key = 'JlI8DAgbDIWiCYFOTl422hVgN/Enj4UsylTv0+MSGFcpXNCwGeJD5UFOJ+44h4KuKxrcbaCgfjL85O5uHZ1y+A=='
    azure_container = 'azurecontainer'
    expiration_secs = None

    def get_key(self):
        return self.account_key

    def get_container(self):
        return self.azure_container

    def get_account_name(self):
        return self.account_name



