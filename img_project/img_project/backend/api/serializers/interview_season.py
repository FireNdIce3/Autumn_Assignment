from backend.models import Season
from rest_framework import serializers

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Season