from django import forms

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


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


class UserResponseForm(forms.ModelForm):

    class Meta:
        model  = UserResponse
        fields = ('text',)
        
        
class DeleteResponseForm(forms.ModelForm):
    
    class Meta:
        model = UserResponse
        fields = []