from django import forms
from .models import UploadingImg
from django.db import models
from django.forms import fields

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadingImg
        fields = ['title_text_img', 'img_file','plastic_type','visible','color']