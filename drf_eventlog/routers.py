from django.conf.urls import url
from rest_framework import routers

from .views import EventLogViewSet

import logging

class EventLogRouter(routers.BaseRouter):

    def __init__(self, prefix=None):
        self.registry = []
        self.prefix = prefix if prefix else 'eventlog'
        self.register(self.prefix, EventLogViewSet)

    def register(self, prefix, viewset, base_name=None):
        if base_name is None:
            base_name = self.get_default_base_name(viewset)
        self.registry= [(prefix, viewset, base_name),]

    def get_default_base_name(self, viewset):
        """
        If `base_name` is not specified, attempt to automatically determine
        it from the viewset.
        """
        queryset = getattr(viewset, 'queryset', None)

        assert queryset is not None, '`base_name` argument not specified, and could ' \
            'not automatically determine the name from the viewset, as ' \
            'it does not have a `.queryset` attribute.'

        return queryset.model._meta.object_name.lower()

    def get_urls(self):
        """
        Return a list of URL patterns, given the registered viewsets.
        """

        ret = []
        ret.append(url('eventlog/(?P<app_name>[a-z]+)/(?P<object_type>[a-z]+)/(?P<object_id>[a-z0-9-]+)/$', EventLogViewSet.as_view(actions={'get': 'get_eventlog_for_obj'}), name="get-eventlog-for-obj"))
        logging.debug({'message': EventLogViewSet.__dict__})
        ret.append(url('eventlog/$', EventLogViewSet.as_view(actions={'get': 'list'}), name="get-eventlog"))
        return ret

    
