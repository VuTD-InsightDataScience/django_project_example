from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(username=email, email=email, password=password, **extra_fields)
