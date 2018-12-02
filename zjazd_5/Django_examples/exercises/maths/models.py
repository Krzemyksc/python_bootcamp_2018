from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Math(models.Model):
    operations = models.CharField(max_length=10)
    a = models.IntegerField()
    b = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE(), null=True, blank=True)
    def __str__(self):
        return f"Math operation: {self.operations}, arguments: {self.a}, {self.b}"
