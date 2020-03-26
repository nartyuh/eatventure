from django.db import models

# Create your models here.
class TestDB(models.Model):
    test = models.CharField(max_length=200, primary_key=True)
    desc = models.CharField(max_length=3)