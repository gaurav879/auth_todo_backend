from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length=255)


# {
#     "username":"gaurav",
#     "email":"tommy@gmail.com",
#     "password":"123"
# }

