import django_filters

from example_app.models import Example


class CreateListExamplesAPIViewFilters(django_filters.FilterSet):
    class Meta:
        model = Example
        fields = ('total',)
