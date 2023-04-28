from django.db import models

# Create your models here.

class Gameuser(models.Model):
    name = models.CharField(max_length=10,primary_key=True)
    c_date = models.DateTimeField()
