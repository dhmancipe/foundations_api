from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .models import Event, Foundation
from .serializers import EventSerializer, FoundationSerializer


class FoundationViewSet(viewsets.ModelViewSet):
    queryset = Foundation.objects.prefetch_related("events")
    serializer_class = FoundationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["location", "sector"]
    search_fields = ["name"]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("foundation")
    serializer_class = EventSerializer