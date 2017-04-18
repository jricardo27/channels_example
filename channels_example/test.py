from channels.test.liveserver import ChannelLiveServerTestCase
from django.test import override_settings

from aloe.testclass import TestCase as AloeTestCase


@override_settings(DEBUG=True, ALLOWED_HOSTS=['*'])
class AloeChannelLiveServerTestCase(ChannelLiveServerTestCase, AloeTestCase):
    """
    Base test class for Django Gherkin tests in conjunction with Channels.
    """

    pass
