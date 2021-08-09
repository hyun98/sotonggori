from rest_framework import serializers
from .models import Organ, Information


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='organ_name.name')

    class Meta:
        model = Information
        fields = ('temp', 'day', 'time', 'name')


