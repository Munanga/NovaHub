from django import forms
from django.forms import TextInput
from upload.models import File
from django.forms import ClearableFileInput


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('uploaded_file',)
#         widgets = {
#             'uploaded_file': ClearableFileInput(attrs={'multiple': True}),
#         }

    # def __init__(self, *args, **kwargs):
    #     super(FileForm, self).__init__(*args, **kwargs)
    #     self.fields['uploaded_file'].widget = TextInput(attrs={
    #         'class': 'form-control-file'})

    def save(self, *args, **kwargs):
        model = super(FileForm, self).save(commit=False)
        file_type = self.files['uploaded_file'].content_type
        model.file_type = file_type
        model.user = args[0]

        model.save()
        return model
        # if commit:
        #     model.save()
        # return model

    # def is_valid(self):
    #     valid = super(FileForm, self).is_valid()
    #     file_size = self.files['uploaded_file'].size
    #     if file_size >= 1000000000:
    #         return False
    #     else:
    #         return True
