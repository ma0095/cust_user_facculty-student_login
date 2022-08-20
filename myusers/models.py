from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)
    options=(
        ("faculty","faculty"),
        ("student","student")
    )
    role=models.CharField(max_length=15,choices=options,default="student")