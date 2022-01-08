from django.db import models


# Create your models here.
class Task(models.Model):
    userid = models.IntegerField(default=0)
    task = models.CharField(max_length=255)
    status = models.BooleanField(max_length=1)


# {
#     "userid":1,
#     "task":"Integrate 2 django apps",
#     "status":0
# }
