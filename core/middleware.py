from functools import partial

from django.db.models import signals
from django.utils.deprecation import MiddlewareMixin


class WhoDidMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = None
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
        if request.method in ('POST', 'PUT', 'PATCH'):
            mark_whodid = partial(self.mark_who_did, user)
            signals.pre_save.connect(
                mark_whodid,
                dispatch_uid=(self.__class__, request, 'pre',),
                weak=False,
            )

    @staticmethod
    def mark_who_did(user, sender, instance, **kwargs):
        if user and hasattr(instance, 'creator_id') and not instance.creator_id:
            instance.creator_id = user.id
        if user and hasattr(instance, 'modifier_id'):
            instance.modifier_id = user.id
