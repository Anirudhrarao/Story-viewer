from re import S
from django import forms
from .models import Status

class AddStoryForm(forms.ModelForm):
    class Meta:
        model=Status
        fields ='__all__'