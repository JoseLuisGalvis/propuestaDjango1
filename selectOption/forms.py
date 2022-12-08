from django import forms
from .models import SelectOption

class SelectForm(forms.ModelForm):
    
    class Meta:
        model = SelectOption
        fields = ['contact_type']