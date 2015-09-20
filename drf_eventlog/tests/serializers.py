from rest_framework import serializers

from .models import TestAutoIncrementModel, TestUUIDPKModel


class TestAutoIncrementModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestAutoIncrementModel


class TestUUIDPKModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestUUIDPKModel
