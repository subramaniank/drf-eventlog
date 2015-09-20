from django.contrib.contenttypes.models import ContentType

from .models import Log


class EventLogger(object):
    """
    Utility class for event logging in the model.
    """

    def log(self, event, obj, details=None):
        event_log = Log()
        event_log.event = event
        event_log.details = details

        if obj is not None:
            content_type = ContentType.objects.get_for_model(obj)
            event_log.obj = content_type
            object_id = obj.pk

        event_log.object_id = object_id
        event_log.save()
        return event_log

eventlogger = EventLogger()
