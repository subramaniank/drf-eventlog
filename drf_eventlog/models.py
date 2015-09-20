import time

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .signals import event_logged


class Log(models.Model):
    """
    A journal model for logging changes to different objects and events in a database.
    """

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.CharField(max_length=36, null=True)
    obj = GenericForeignKey("content_type", "object_id")
    event = models.CharField(max_length=50, db_index=True)
    details = models.TextField(null=True)
    timestamp = models.BigIntegerField(db_index=True)

    class Meta:
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        self.timestamp = time.time()
        event_logged.send_robust(sender=Log, event=self)
        super(Log, self).save(*args, **kwargs)
