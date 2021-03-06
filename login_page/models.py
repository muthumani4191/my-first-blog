from django.db import models
from django.utils import timezone

class SignUp(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=15)
    repeat_password = models.CharField(max_length=15)
    login_date = models.DateTimeField(
            default=timezone.now)

class LogIn(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=15)



