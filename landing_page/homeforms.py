from django import forms
from .models import NewsLetter


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('news_email',)

        widgets = {
            'news_email' : forms.TextInput(attrs={'placeholder': 'Enter your email'}),
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['news_email'].label = ''
