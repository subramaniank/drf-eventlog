from rest_framework import viewsets

from .serializers import LogSerializer

from .models import Log


class EventLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple read only view set for event logs
    """

    queryset = Log.objects.all()
    serializer_class = LogSerializer


