from django import forms
from .models import *
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class AdForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=True)
    upload = RichTextUploadingField()

    class Meta:
        model  = Ad
        fields = ('title', 'category', 'text', 'upload', 'category')
        

class DeleteForm(forms.ModelForm):
    
    class Meta:
        model = Ad
        fields = []