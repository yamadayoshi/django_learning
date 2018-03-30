from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    users = models.OneToOneField(User, on_delete=None);

    #addicional
    portifolio_site = models.URLField(blank=True)

    portifolio_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.users.username
