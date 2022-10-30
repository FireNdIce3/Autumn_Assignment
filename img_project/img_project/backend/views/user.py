from backend.api.serializers.img_member import ImgMemberSerializer
from backend.models import ImgMember
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = ImgMemberSerializer

    def get_queryset(self):
        return ImgMember.objects.filter(username = self.request.user.username)