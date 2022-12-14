from backend.models import Question
from rest_framework import serializers
from .img_member import ImgMemberSerializer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionDetailsSerializer(serializers.ModelSerializer):
    assignee_details = serializers.SerializerMethodField("get_assignee_details")

    def get_assignee_details(self, instance):
        assignee_queryset = instance.assignee
        return ImgMemberSerializer(assignee_queryset, many=True).data

    class Meta:
        fields = '__all__'
        model = Question