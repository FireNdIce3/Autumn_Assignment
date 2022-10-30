from rest_framework import viewsets
from backend.models import InterviewSection
from backend.api.serializers.interview import InterviewSectionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class InterviewSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = InterviewSectionSerializer
    queryset = InterviewSection.objects.all()