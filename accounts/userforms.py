from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "Email Address"

    def save(self, commit=True):
        instance = super(UserSignUpForm, self).save(commit=commit)
        self.send_email()
        return instance

    def send_email(self):
        email = self.cleaned_data.get('email',None)
        first_name = self.cleaned_data.get('first_name', None)
        last_name = self.cleaned_data.get('last_name', None)
        subject = 'Eddies account created'
        html_message = render_to_string('accounts/mail_template.html', {'first_name': first_name, 'last_name':last_name })
        plain_message = strip_tags(html_message)
        from_email = 'eddies.startup@gmail.com'
        to = email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)





        # 
        # subject, from_email, to = 'hello', 'eddies.startup@gmail.com', email
        # text_content = 'This is an important message.'
        # html_content = '<p>This is an <strong>{{ name }}</strong> message.</p>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()

    # def send_email(self):
    #     email = self.cleaned_data.get('email',None)
    #     name = self.cleaned_data.get('first_name', None)
    #     msg = EmailMessage(
    #         'Activate eddies account',
    #         'Dear,\n\nThank you for joining Us. Click this link to validate your eddies account:\n\nLink\n\nBest Regards,\nEddies Team.\neddies.startup@gmail.com',
    #         'noreply@eddies.com',
    #         ['refriansyari@gmail.com',email],
    #         )
    #     msg.send()

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('company_name', 'company_url','affiliation','country',)
        exclude =('user',)
    
        widgets = {
            'company_name' : forms.TextInput(attrs={'placeholder': 'Enter Company/Institution Name'}),
            'company_url' : forms.URLInput ( attrs={'placeholder': 'https://www.example.com'}),
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['company_name'].label = 'Company or institution name'
        self.fields['company_url'].label = "Company or institution URL (ex: https://www.example.com)"
        self.fields['affiliation'].label = "Affiliation"
        self.fields['country'].label = "Country"

class UserAccountForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name','username','email')