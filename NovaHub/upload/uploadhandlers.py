# from django.core.files.uploadhandler import FileUploadHandler
# import os, uuid
# from azure.storage.blob import BlobServiceClient, __version__
#
#
# def connect_to_azure() -> BlobServiceClient:
#     blob_service_client = []
#     try:
#         print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
#
#         # connection string is stored in an environment variable on the machine
#         connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
#
#         # Create the BlobServiceClient object which will be used to create a container client
#         blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#     except Exception as ex:
#         print('Exception:')
#         print(ex)
#
#     return blob_service_client
#
#
# '''
# def upload_to_azure(data):
#     try:
#         container_name = "jacke9ced004-1103-414f-9848-6a66efe0c48c"
#         blob_client = connect_to_azure().get_blob_client(container=container_name)
#
#         blob_client.upload_blob(data)
#     except Exception as ex:
#         print('Exception:')
#         print(ex)
# '''
#
#
# class AzureUploadHandler(FileUploadHandler):
#
#     def receive_data_chunk(self, raw_data, start):
#
#         try:
#
#             container_name = "jacke9ced004-1103-414f-9848-6a66efe0c48c"
#             #file = open(raw_data, newline='', encoding="utf8")
#             #x = self.file_name#.FILES['uploaded_file'].name
#             #print(x)
#             #print(self.field_name)
#             #print(os.path.abspath(file))
#             blob_client = connect_to_azure().get_blob_client(container=container_name, blob=self.file_name)
#             blob_client.upload_blob(raw_data)
#             # for data in raw_data:
#             #     blob_client.upload_blob(data)
#         except Exception as ex:
#             print('Exception:')
#             print(ex)
#
#
#
#
#     def file_complete(self, file_size):
#         """
#         Return a file object if we're activated.
#         """
#         print("Complete: AzureUploadHandler")
#
#
