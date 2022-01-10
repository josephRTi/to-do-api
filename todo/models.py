from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Node(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    node = models.CharField(max_length=1000)
    date = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
