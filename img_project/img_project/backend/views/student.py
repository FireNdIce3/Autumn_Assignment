from rest_framework import viewsets
from backend.api.serializers.student import StudentSerializer
from backend.models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class studentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter ]
    search_fields = ['name', 'enrolment_number', ]
    ordering_fields = ['name', ]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()