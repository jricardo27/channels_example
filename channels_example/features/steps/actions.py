from urllib.parse import urljoin

from aloe import step
from aloe_django import django_url


@step(r'I visit site page "([^"]*)"')
def visit_page(self, page):
    """Visit the specific page of the site."""

    address = django_url(self)

    url = urljoin(address, page)
    self.given('I visit "%s"' % url)
