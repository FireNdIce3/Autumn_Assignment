import imp
from backend.models import Section
from rest_framework import serializers
from .question import QuestionDetailsSerializer


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class SectionWithQuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField("get_questions")

    def get_questions(self, instance):
        return QuestionDetailsSerializer(instance.question_set, many=True).data

    class Meta:
        model = Section
        fields = '__all__'