from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.settings import api_settings

from .models import Log
from .serializers import LogSerializer

from django.contrib.contenttypes.models import ContentType

class EventLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple read only view set for event logs
    """

    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def get_eventlog_for_obj(self, request, app_name, object_type, object_id, *args, **kwargs):
        content_type = ContentType.objects.get(app_label=app_name, model=object_type)
        content_obj = content_type.get_object_for_this_type(pk=object_id)
        queryset = Log.objects.filter(content_type__pk=content_type.pk,object_id=content_obj.pk)
        logserializer = LogSerializer(queryset, many=True)
        return Response(data=logserializer.data, status=status.HTTP_200_OK)
