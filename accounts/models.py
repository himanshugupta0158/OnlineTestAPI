from time import timezone
from tkinter import Widget
from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin
from django.forms import PasswordInput
from django.utils.translation import gettext_lazy
from django.utils import timezone

from accounts.CustomAccountManager import CustomAccountManager
# Create your models here.

# Custom User Model : it implemented version of existing django User model as our required model.
class CustomUser(AbstractUser,PermissionsMixin):
    email = models.EmailField(gettext_lazy('Email Address'),unique=True)
    username = models.CharField(max_length=50,unique=True)
    firstname = models.CharField(max_length=50 , blank=True)
    lastname = models.CharField(max_length=50 ,blank=True)
    start_date = models.DateField(default=timezone.now)
    about = models.TextField(gettext_lazy('About'),max_length=500,blank=True)
    is_examiner = models.BooleanField(default=False)
    is_examinee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Creating objects of CustomAccountManager
    objects = CustomAccountManager()
    
    # required field using which User identify itself
    USERNAME_FIELD = 'username'
    
    # other required fields need to be there for our use.
    REQUIRED_FIELDS = ['email','firstname','lastname']
    
    def __str__(self) :
        return self.username
