from django.contrib.auth import get_user_model

User = get_user_model()


def log_status(function):
    def wrapper(self, *args, **kwargs):
        return_value = function(self, *args, **kwargs)  # do whatever you want here
        return return_value
    return wrapper
