from django.db import models
from .student import Student
from .question import Question

class Marks(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField(verbose_name="Marks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100, blank = True, null = True)