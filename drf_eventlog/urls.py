from rest_framework import routers

from .views import EventLogViewSet

eventlog_router = routers.DefaultRouter()
eventlog_router.register('eventlog', EventLogViewSet)
