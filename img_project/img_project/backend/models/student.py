from django.db import models
from .selection_round import Round

class Student(models.Model):
    role_choices = [
        ('developer', "Developer"),
        ('designer', "Designer")
    ]
    status_choices = [
        ('Evaluated', "Evaluated"),
        ('Not Evaluated', "Not Evaluated"),
        ('Yet to be Called', "Yet to be Called")
    ]

    name = models.CharField(max_length=300)
    enrol_no = models.BigIntegerField(null=False, unique=True)
    branch = models.CharField(max_length=300)
    mobile = models.CharField(max_length=10)
    status = models.CharField(max_length=300, null=True,
    choices=status_choices)
    stage = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=300, choices=role_choices)
    email = models.EmailField()
    year = models.IntegerField()
    round = models.ManyToManyField(Round, related_name="students",
    related_query_name="student", blank=True)
    
    def __str__(self) -> str:
        return self.name + ' (' + str(self.enrolment_number) + ')'