from django import forms
from.models import LunBo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = LunBo
        fields = ['name','description','image']

