from django.db import models
from django.db.models.indexes import Index
from django.utils.translation import gettext as _
from model_utils.models import SoftDeletableModel, StatusModel, TimeStampedModel

from core.mixins import TrackRecordChangeByMixin
from example_app.constants import ExampleStatus


class Example(TrackRecordChangeByMixin, TimeStampedModel, SoftDeletableModel, StatusModel):
    STATUS = ExampleStatus.choices()

    name = models.CharField(max_length=255, blank=True, default=None)
    total = models.IntegerField(default=0, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
        indexes = [Index(fields=['-id', '-name'])]
        permissions = ()
        default_permissions = ()
        db_table = 'example'
