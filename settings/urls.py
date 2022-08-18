from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('examples/', include('example_app.urls'))
]

urlpatterns += [
    path('public-api/', include('core.public_api', namespace='public-api')),
    path('private-api/', include('core.private_api', namespace='private-api')),
]
