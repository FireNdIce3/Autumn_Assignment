from rest_framework import viewsets
from backend.models import Panelists
from backend.api.serializers.panel import PanelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class PanelViewSet(viewsets.ModelViewSet):
   
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = PanelSerializer
    queryset = Panelists.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter ]
    search_fields = ['place', ]
    filterset_fields = ['available', 'status', ]
    ordering_fields = '__all__'