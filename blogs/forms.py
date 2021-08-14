from django import forms
from django.db.models.base import Model
from .models import *
from django.forms import ModelForm

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'