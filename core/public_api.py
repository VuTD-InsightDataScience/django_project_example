from example_app.api.public.urls import urlpatterns as hotel_urls

app_name = 'public-api'

urlpatterns = []
urlpatterns += hotel_urls
