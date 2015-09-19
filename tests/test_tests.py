from django.db import models
from drf_eventlog.logger import eventlogger as eventlogger
from django.db.models.loading import cache

import pytest

import logging
 
logging.basicConfig(level=logging.DEBUG)

from drf_eventlog.models import Log
from drf_eventlog.tests.models import TestAutoIncrementModel

class TestEventLog(object):


    @pytest.mark.django_db
    def test_autoincrement_model(self):
        log = logging.getLogger('test_autoincrement')
        test_auto_increment = TestAutoIncrementModel()
        test_auto_increment.name = "Subramanian"
        test_auto_increment.rank = 1
        test_auto_increment.clash = True
        test_auto_increment.save()

        eventlogger.log("CREATED",test_auto_increment,"A new object was created here")
        
