from django import forms
from .models import forfile

class forfileform(forms.ModelForm):
    class Meta:
        model = forfile
        fields = ('file_name','file_link')
        exclude = ('user',)

        widgets = {
            'file_name' : forms.TextInput(attrs={'id': 'name-field', 'placeholder': 'Enter file name'}),
            'file_link' : forms.FileInput(attrs={'id': 'link-field', 'placeholder': 'Enter file name'}),
        }
