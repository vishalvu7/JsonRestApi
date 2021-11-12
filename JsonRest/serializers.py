from rest_framework import serializers

from JsonRest.models import JsonData

class JsonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonData
        fields = ('data')
        
        