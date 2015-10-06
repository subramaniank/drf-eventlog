import json
import logging
import uuid

import pytest
from rest_framework.renderers import JSONRenderer

from drf_eventlog.logger import eventlogger as eventlogger
from drf_eventlog.tests.models import TestAutoIncrementModel, TestUUIDPKModel
from drf_eventlog.tests.serializers import TestUUIDPKModelSerializer

logging.basicConfig(level=logging.DEBUG)


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
        assert response.status_code == 200

        response = client.get('/eventlog/tests/testuuidpkmodel/{0}/'.format(test_uuid_pk.pk))
        assert response.status_code == 200
        resp = json.loads(response.content)
        assert resp[0]['object_id'] == test_uuid_pk.pk
        assert resp[0]['details'] == "Creation of object"

        assert resp[1]['object_id'] == test_uuid_pk.pk
        assert resp[1]['details'] == model_json
        #== '[{"id":1,"object_id":"c04abde9-fc58-4226-a96c-ad5015fbf1e8","event":"CREATED","details":"Creation of object","timestamp":1444133659,"content_type":3},{"id":2,"object_id":"c04abde9-fc58-4226-a96c-ad5015fbf1e8","event":"UPDATING","details":"{\\"id\\":\\"c04abde9-fc58-4226-a96c-ad5015fbf1e8\\",\\"text\\":\\"Text changed\\"}","timestamp":1444133659,"content_type":3}]'
