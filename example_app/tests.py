import pytest
from django.test import TestCase

from example_app.models import Example
from example_app.serializers import ExampleDataSerializer


class TestExampleSerializers(TestCase):
    pytestmark = pytest.mark.django_db

    def set_up(self):
        self.example = Example.objects.create()

    def test_serializer_contains_expected_fields(self):
        self.set_up()
        data = ExampleDataSerializer(instance=self.example).data
        fields = ['id', 'name']
        assert set(data.keys()) == set(fields)
