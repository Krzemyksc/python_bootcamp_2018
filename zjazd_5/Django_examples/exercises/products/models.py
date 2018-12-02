from django.db import models

# Create your models here.
class Products(models.Model):
    operation = models.Charfield(max_length=100)
