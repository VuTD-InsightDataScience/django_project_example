from django.contrib import admin

from example_app.models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['name', 'total']
