from django.contrib.auth.forms import PasswordChangeForm
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

username = "admin"
password = "admin"


class Dboard(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    
    phone = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name



class UserForm(User):
    email = models.EmailField(primary_key=True,unique=True),
    ID = models.CharField(max_length=3, primary_key=True)