from django import forms
from.models import AdverTise

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = AdverTise
        fields = ['name','capital','duration','image']

