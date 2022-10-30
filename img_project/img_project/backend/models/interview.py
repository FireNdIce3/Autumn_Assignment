from django.db import models
from .selection_round import Round

class InterviewSection(models.Model):
    type_choices = [
        ('TI', "Techincal Interview"),
        ('HI' , "HR Interview")
    ]
    
    title = models.CharField(max_length=50)
    round = models.ForeignKey(Round, on_delete=models.CASCADE,
    related_name="interview_sections")
    type = models.CharField(max_length=5, choices=type_choices)
    maximum_marks = models.IntegerField()