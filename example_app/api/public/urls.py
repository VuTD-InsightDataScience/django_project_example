from django.urls import path

from example_app.api.public import examples as example_views

urlpatterns = []

# Hotel urls
urlpatterns += [
    path('examples/',
         view=example_views.CreateListExamplesAPIView.as_view({'get': 'list', 'post': 'create'}),
         name='create-list-example-view-set'),
    path('custom-examples/',
         view=example_views.CreateListExamplesAPIView.as_view({'get': 'get_list_hotels'}),
         name='custom-examples-view-set'),
    path('example/<int:pk>/',
         view=example_views.RetrieveUpdateDestroyExampleAPIView.as_view(
             {'get': 'get', 'put': 'update', 'delete': 'destroy'}
         ),
         name='retrieve-update-destroy-example-view-set'),
]
