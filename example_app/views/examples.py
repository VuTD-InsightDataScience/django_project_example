from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from core.mixins import APIMixin
from core.pagination import StandardPageNumberPagination
from example_app.constants import ExampleStatus
from example_app.filters import CreateListExamplesAPIViewFilters
from example_app.models import Example
from example_app.serializers import (CreateExampleDataSerializer, CustomExampleDataSerializer, ExampleDataSerializer)


class CreateListExamplesAPIView(APIMixin, viewsets.GenericViewSet, generics.ListCreateAPIView):
    pagination_class = StandardPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = CreateListExamplesAPIViewFilters
    search_fields = ('name',)
    ordering = ('name',)

    def get_queryset(self):
        return Example.objects.all()

    def get_serializer_class(self):
        if self.action in ['get_list_hotels']:
            return CustomExampleDataSerializer
        if self.action in ['create']:
            return CreateExampleDataSerializer
        return ExampleDataSerializer

    def get_permissions(self):
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def get_list_hotels(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        status_display = request.data.pop('status_display')
        request.data['status'] = dict({y: x for (x, y) in ExampleStatus.choices()}).get(status_display)
        return super().create(request, *args, **kwargs)


class RetrieveUpdateDestroyExampleAPIView(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Example.objects.all()

    def get_serializer_class(self):
        return ExampleDataSerializer

    def check_object_permissions(self, request, obj):
        return super().check_object_permissions(request, obj)
