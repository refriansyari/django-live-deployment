from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class UserProfile(models.Model):
    
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    company_url = models.URLField(max_length=50, blank=True)
    country = CountryField(null=True)
    
    AFF_CHOICES = (('Academic','Academic'),
                    ('Bussiness','Bussiness'),
                    ('Non-profit','Non-profit'),
                    ('Industry/Government','Industry/Government'))

    affiliation = models.CharField(max_length=50, choices=AFF_CHOICES, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, default='profile_picture/defaultphoto.png')

    def __str__(self):
        return str(self.user)