import os

from urllib.parse import urljoin

# Import steps from `aloe_webdriver`
import aloe_webdriver
import aloe_webdriver.screenshot_failed

from aloe import step
from aloe_django import django_url


@step(r'I visit site page "([^"]*)"')
def visit_page(self, page):
    """Visit the specific page of the site."""

    address = django_url(self)

    if 'SERVER_HOST' in os.environ:
        port = address.split(':')[-1]

        address = 'http://{host}:{port}'.format(
            host=os.environ['SERVER_HOST'],
            port=port,
        )

    url = urljoin(address, page)
    self.given('I visit "%s"' % url)
