from django.urls import path
from example_app import views

urlpatterns = [
    path("", views.excel_formula, name="excel-formula")
]
