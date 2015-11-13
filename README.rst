.. image:: https://travis-ci.org/subramaniank/drf-eventlog.svg?branch=master
   :target: https://travis-ci.org/subramaniank/drf-eventlog

.. image:: https://coveralls.io/repos/subramaniank/drf-eventlog/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/subramaniank/drf-eventlog?branch=master

.. image:: https://badge.fury.io/py/drf_eventlog.svg
   :target: http://badge.fury.io/py/drf_eventlog


=========
drf-eventlog
=========

EventLog app with DRF APIs to quickly track events and query them
----------

**Installation and Configuration**

.. code-block:: python
		pip install drf_eventlog


Add ``drf_eventlog``, ``django_filters``, and ``rest_framework`` to ``INSTALLED_APPS`` in your django ``settings.py``

.. code-block:: python
		python manage.py migrate

Migrate DB to create drf_eventlog db models.

**Usage**

.. code-block
    def log(self, event, obj, details=None):


``log`` method takes an event name/tag, the ``obj`` is the object in reference to which the audit event happens.
In addition, details is a TextField.

.. code-block:: python
		from drf_eventlog.logger import eventlogger
		eventlogger.log("UPDATING", test_uuid_pk, model_json)
