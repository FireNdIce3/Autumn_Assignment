from django.db import models
from .student import Student
from .panel import Panelists
from .selection_round import Round

class Interview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panelists, on_delete=models.SET_NULL, null = True) # SET_NULL
    time_assigned = models.DateTimeField(null = True, blank=True)
    time_entered = models.DateTimeField(null = True, blank=True)
    completed = models.BooleanField(default=False)
    round = models.ForeignKey(Round, on_delete=models.CASCADE,
    related_name="interviews")
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.student} -{self.round}'