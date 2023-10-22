from rest_framework import generics

from recommendations.serializers import EventAdressSerializer
from recommendations.models import Events


class EventCoordinates(generics.RetrieveAPIView):
    serializer_class = EventAdressSerializer
    queryset = Events.objects.all()


class EventCoordinatesList(generics.ListAPIView):
    serializer_class = EventAdressSerializer
    queryset = Events.objects.all()