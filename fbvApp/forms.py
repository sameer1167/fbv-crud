from django import forms
from fbvApp.models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
