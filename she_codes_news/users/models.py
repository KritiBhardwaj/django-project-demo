from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    #this is where I would put custom fields
    # pass

    About_Me = models.TextField(max_length=500,blank=True)
    user_image= models.CharField(max_length=3000,blank=True, null=True)

    def __str__(self):
        return self.username



