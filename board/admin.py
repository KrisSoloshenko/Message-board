from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class AdAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Ad
        fields = '__all__'


class AdAdmin(admin.ModelAdmin):
    form = AdAdminForm


admin.site.register(Ad, AdAdmin)
admin.site.register(UserResponse)
