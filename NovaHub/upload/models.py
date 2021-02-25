from django.db import models
from upload.custom_azure import AzureMediaStorage
from azure.storage.blob import BlockBlobService, ContainerPermissions
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from upload.services import get_file_size, image, video, audio, archive, document


# Instantiate AzureMediaStorage
azure_media_storage = AzureMediaStorage()

# get account name
account_name = azure_media_storage.get_account_name()

# get account key
account_key = azure_media_storage.get_key()

# get container name
container_name = azure_media_storage.get_container()


class File(models.Model):
    uploaded_file = models.FileField(storage=AzureMediaStorage(), max_length=300, blank=False)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file_type = models.CharField(max_length=50, blank=False, default="Unknown")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.uploaded_file.name

    @property
    def get_name(self):
        return self.uploaded_file.name

    @property
    def get_size(self):
        return self.uploaded_file.size

    @property
    def get_url(self):
        return self.uploaded_file.url

    @property
    def content_type(self):
        return self.file_type

    def get_unit_size(self):
        return get_file_size(self.get_size)

    def get_type_name(self, mime_type):

        if mime_type in image:
            return "image"
        elif mime_type in audio:
            return "audio"
        elif mime_type in video:
            return "video"
        elif mime_type in document:
            return "document"
        elif mime_type in archive:
            return "archive"

        return "generic"

    # Method to return the file type
    # as string e.g image, audio etc
    def return_type(self):
        return self.get_type_name(self.content_type)

    # Method to get the Blob URI
    # in the Azure storage account
    def get_sas_url(self):
        block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
        permission = ContainerPermissions(read=True)
        sas = block_blob_service.generate_container_shared_access_signature(container_name,
                                                                            permission,
                                                                            datetime.utcnow() + timedelta(hours=1))
        blob_url = "https://novahub.blob.core.windows.net/azurecontainer/" + \
                   self.uploaded_file.name + "?" + sas

        return blob_url

    # Method to delete a file both in the
    # DataBase and on the Azure storage account
    def delete(self, *args, **kwargs):

        try:
            file = self.uploaded_file.name
            block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
            block_blob_service.delete_blob(container_name=container_name, blob_name=self.uploaded_file.name)
            print("Deleted file: ", file)

        except Exception as ex:
            print('Exception:')
            print(ex)

        super(File, self).delete(*args, **kwargs)
