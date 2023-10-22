from rest_framework import serializers

from recommendations.models import Events


class EventAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'adress', 'latitude', 'longtitude']
