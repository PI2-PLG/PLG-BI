from modules.models import ModuleData
from rest_framework import serializers

class ModuleDataSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    latitude = serializers.DecimalField(max_digits=11, decimal_places=8)
    longitude = serializers.DecimalField(max_digits=11, decimal_places=8)
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    humidity = serializers.DecimalField(max_digits=5, decimal_places=2)
    velocity = serializers.DecimalField(max_digits=5, decimal_places=2)
    ppm = serializers.IntegerField()

    class Meta:
        model = ModuleData
        fields = ['date','latitude','longitude','temperature', 'humidity', 'velocity', 'ppm']