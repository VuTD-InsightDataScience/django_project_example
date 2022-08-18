from functools import partial

from django.db.models import signals
from django.utils.deprecation import MiddlewareMixin


class WhoDidMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = None
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
        if request.method in ('POST', 'PUT', 'PATCH'):
            mark_who_did = partial(self.mark_who_did, user)
            signals.pre_save.connect(
                mark_who_did,
                dispatch_uid=(self.__class__, request, 'pre',),
                weak=False
            )
        if request.method in ('DELETE',):
            mark_who_deleted = partial(self.mark_who_deleted, user)
            signals.pre_delete.connect(
                mark_who_deleted,
                dispatch_uid=(self.__class__, request, 'pre',),
                weak=False
            )

    @staticmethod
    def mark_who_did(user, sender, instance, **kwargs):
        if user and hasattr(instance, 'creator_id') and not instance.creator_id:
            instance.creator_id = user.id
        if user and hasattr(instance, 'updated_by_id'):
            instance.updated_by_id = user.id

    @staticmethod
    def mark_who_deleted(user, sender, instance, **kwargs):
        if user and hasattr(instance, 'removed_by_id'):
            instance.removed_by = user.id
