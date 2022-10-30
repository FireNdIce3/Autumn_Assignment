from backend.models import SectionMarks
from rest_framework import serializers



class SectionMarksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SectionMarks