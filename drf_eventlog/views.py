from rest_framework import viewsets
from rest_framework.settings import api_settings

from .models import Log
from .serializers import LogSerializer


class EventLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple read only view set for event logs
    """

    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    queryset = Log.objects.all()
    serializer_class = LogSerializer
