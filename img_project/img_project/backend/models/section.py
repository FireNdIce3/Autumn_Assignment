from django.db import models
from .test_details import Test

class Section(models.Model):
    title = models.CharField(max_length=50)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)