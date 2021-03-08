from django import forms
from .models import FilesUpload


class UploadForm(forms.ModelForm):
    class Meta: 
        model = FilesUpload
        fields = ['file']