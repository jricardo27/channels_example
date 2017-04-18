from channels.test.liveserver import ChannelLiveServerTestCase
from django.test import override_settings

from aloe.testclass import TestCase as AloeTestCase


@override_settings(DEBUG=True)
class TestCase(ChannelLiveServerTestCase, AloeTestCase):
    """
    Base test class for Django Gherkin tests in conjunction with Channels.
    """

    pass
