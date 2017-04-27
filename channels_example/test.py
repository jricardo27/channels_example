from channels.test.liveserver import ChannelLiveServerTestCase
from django.db import connections
from django.test import override_settings

from aloe.testclass import TestCase as AloeTestCase


@override_settings(DEBUG=True)
@override_settings(ALLOWED_HOSTS=['*'])
@override_settings(EMAIL_BACKEND='channels_example.mail.EmailBackend')
class TestCase(ChannelLiveServerTestCase, AloeTestCase):
    """
    Base test class for Django Gherkin tests in conjunction with Channels.
    """

    def _pre_setup(self):
        # Close all DB connections before running Worker and Daphne processes.
        connections.close_all()

        super()._pre_setup()
