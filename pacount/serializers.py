from rest_framework import serializers
from pacount.models import Field, Hole


class HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hole
        fields = ['number', 'par']


class FieldListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['name', 'city']


class FieldSerializer(serializers.ModelSerializer):
    holes = HoleSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ['name', 'holes']