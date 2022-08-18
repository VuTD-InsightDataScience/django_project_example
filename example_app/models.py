from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.indexes import Index
from django.utils.translation import gettext as _
from model_utils.models import SoftDeletableModel, StatusModel, TimeStampedModel

from core.mixins import TrackRecordChangeByMixin
from example_app.constants import ExampleStatus

User = get_user_model()


class Example(TrackRecordChangeByMixin, TimeStampedModel, SoftDeletableModel, StatusModel):
    STATUS = ExampleStatus.choices()

    name = models.CharField(max_length=255, blank=True, default=None)
    total = models.IntegerField(default=0, null=True)

    creator = models.ForeignKey(User, related_name="creator_example", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name="updated_by_example", on_delete=models.CASCADE)
    removed_by = models.ForeignKey(User, related_name="removed_by_example", on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
        indexes = [Index(fields=['-id', '-name'])]
        permissions = ()
        default_permissions = ()
        db_table = 'example'
