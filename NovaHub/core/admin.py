from django.contrib import admin
from upload.models import File
from django.contrib import admin
from users.models import Profile

admin.site.register(Profile)


@admin.register(File)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "uploaded_file", "get_url", "get_size", "date_uploaded", "updated_at")



def delete_model(File, request):
    pass
    # try:
    #     file = self.uploaded_file.name
    #     block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
    #     block_blob_service.delete_blob(container_name=container_name, blob_name=self.uploaded_file.name)
    #     print("Deleted file: ", file)
    #
    # except Exception as ex:
    #     print('Exception:')
    #     print(ex)
    #
    # super(File, self).delete(*args, **kwargs)