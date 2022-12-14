from rest_framework import serializers
from backend.models import ImgMember

class ImgMemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "enrolment_number", "name", "username", "year", "email", "image", "is_master"]
        model = ImgMember

class ImgMemberNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name", "is_master"]
        model = ImgMember

