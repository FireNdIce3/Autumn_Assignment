from backend.models import Marks
from rest_framework import serializers



class MarksSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = Marks