from .student import Student
from .img_member import ImgMember
from .interview_details import Interview
from .interview import InterviewSection
from .panel import Panelists
from .question import Question
from .selection_round import Round
from .marks import Marks
from .interview_season import Season
from .section import Section
from .section_marks import SectionMarks
from .test_details import Test
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    