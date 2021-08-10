from django import forms
from .models import Organ, Information

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['organ_name', 'temp']
