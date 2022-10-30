from django.db import models
from .img_member import ImgMember

class Panelists(models.Model):
    status_choices = [
        ('NA', "Not Available"),
        ('Available', "Available")
    ]
    place = models.CharField(max_length=100)
    available = models.BooleanField()
    status = models.CharField(max_length=50, choices=status_choices)
    members = models.ManyToManyField(ImgMember, blank = True)

    def __str__(self) -> str:
        return self.place