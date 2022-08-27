from django.db import models
from django.utils import timezone

# Create your models here.


class SignUp(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    # profile_pic = models.ImageField(upload_to="" default="")

    def __str__(self):
        return self.username
