from django.db import models
from drf_eventlog.logger import eventlogger as eventlogger
from django.db.models.loading import cache

import pytest

import logging
 
logging.basicConfig(level=logging.DEBUG)

from drf_eventlog.models import Log
from drf_eventlog.tests.models import TestAutoIncrementModel

logger = logging.getLogger('test_eventlog')

class TestEventLog(object):

    @pytest.mark.django_db
    def test_autoincrement_model(self):

        test_auto_increment = TestAutoIncrementModel()
        test_auto_increment.name = "Subramanian"
        test_auto_increment.rank = 1
        test_auto_increment.clash = True
        test_auto_increment.save()
        eventlogger.log("CREATED",test_auto_increment,"A new object was created here")


    @pytest.mark.django_db
    def test_client(self, client):
        logger.debug('What the ')
        response = client.get('/eventlog/')
        assert response.status_code == 200


