from django.db import models

# Create your models here.
class country(models.Model):
    name = models.TextField()
    cases = models.IntegerField()
    dies = models.IntegerField()