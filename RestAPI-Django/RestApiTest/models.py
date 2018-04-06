from django.db import models

# Create your models here.
class RestTest(models.Model):
    message = models.CharField(max_length=30)