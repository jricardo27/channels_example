from django.test import override_settings

from aloe_django import TestCase as AloeTestCase


@override_settings(DEBUG=True)
class TestCase(AloeTestCase):
    """Base test class for Django Gherkin tests with DEBUG enabled."""

    pass
