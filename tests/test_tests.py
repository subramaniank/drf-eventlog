import json
import logging
import uuid

import pytest
from rest_framework.renderers import JSONRenderer

from drf_eventlog.logger import eventlogger as eventlogger
from drf_eventlog.tests.models import TestAutoIncrementModel, TestUUIDPKModel
from drf_eventlog.tests.serializers import TestUUIDPKModelSerializer

logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger('test_eventlog')


@pytest.mark.django_db
class TestEventLog(object):

    def test_autoincrement_model(self, client):

        test_auto_increment = TestAutoIncrementModel()
        test_auto_increment.name = "Subramanian"
        test_auto_increment.rank = 1
        test_auto_increment.clash = True
        test_auto_increment.save()
        eventlogger.log("CREATED", test_auto_increment, "A new object was created here")

        response = client.get('/eventlog/')
        assert response.status_code == 200
        resp_dict = json.loads(response.content.decode('ascii'))
        assert len(resp_dict) == 1
        first_obj = resp_dict[0]
        assert first_obj['object_id'] == "1"
        assert first_obj['event'] == "CREATED"
        assert first_obj['details'] == "A new object was created here"

    def test_uuid_pk_model(self, client):

        test_uuid_pk = TestUUIDPKModel()
        test_uuid_pk.id = str(uuid.uuid4())
        test_uuid_pk.text = "This is a new UUID"
        test_uuid_pk.save()

        eventlogger.log("CREATED", test_uuid_pk, "Creation of object")

        test_uuid_pk.text = "Text changed"

        serialized_data = TestUUIDPKModelSerializer(instance=test_uuid_pk).data
        model_json = JSONRenderer().render(serialized_data)
        eventlogger.log("UPDATING", test_uuid_pk, model_json)

        response = client.get('/eventlog/')
        logger.debug(response.content)
        assert response.status_code == 200
