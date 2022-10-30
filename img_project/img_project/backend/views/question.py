from rest_framework import viewsets, status
from backend.api.serializers.question import QuestionSerializer, QuestionDetailsSerializer
from backend.models import Question
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class QuestionViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = QuestionDetailsSerializer
    queryset = Question.objects.all()

    def create(self, request):
        """
        To create Question instance, request.data should include section, title, maximum_marks, assignee(optional)
        """
        request_data = request.data
        serialized_data = QuestionSerializer(data = request_data)
        if serialized_data.is_valid():
            self.perform_create(serialized_data)
            return Response(serialized_data.data, status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,
             status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serialized_data):
        serialized_data.save()