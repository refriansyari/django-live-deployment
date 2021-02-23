from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model

class NewsLetter(models.Model):
    news_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.news_email