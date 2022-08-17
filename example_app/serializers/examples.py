from rest_framework import serializers

from example_app.models import Example


class ExampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'name')
        read_only_fields = ('id',)


class CustomExampleDataSerializer(ExampleDataSerializer):
    class Meta:
        model = Example
        fields = ExampleDataSerializer.Meta.fields + ('total', 'status_display',)
        read_only_fields = ExampleDataSerializer.Meta.read_only_fields + ('total', 'status_display')
