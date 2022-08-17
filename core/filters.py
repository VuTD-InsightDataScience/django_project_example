import django_filters
from django import forms
from django.core.exceptions import ValidationError


class CommaSeparatedStringsField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if value and isinstance(value, str):
            value = value.split(',')
        return value


class CommaSeparatedStringsFilter(django_filters.Filter):
    field_class = CommaSeparatedStringsField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('distinct', True)
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)


class ListFieldForm(forms.MultipleChoiceField):
    def valid_value(self, value):
        return True

    def to_python(self, value):
        if not value:
            return []
        elif not isinstance(value, (list, tuple)):
            raise ValidationError(self.error_messages['invalid_list'], code='invalid_list')
        return [str(val) for val in value if val]


class ListFieldFilters(django_filters.Filter):
    field_class = ListFieldForm

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('distinct', True)
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)
