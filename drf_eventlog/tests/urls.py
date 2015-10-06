try:
    from django.conf.urls import patterns, include
except ImportError:
    from django.conf.urls.defaults import patterns, include  # noqa

from drf_eventlog.urls import eventlog_router

urlpatterns = patterns(
    ""
)

urlpatterns += eventlog_router.urls


