import os

from contextlib import contextmanager

from aloe import around, world
from selenium import webdriver
from xvfbwrapper import Xvfb


NPM_BIN_DIR = './node_modules/.bin/'


@around.all
@contextmanager
def with_browser():
    """Start a browser for the tests."""

    if 'XVFB' in os.environ:
        world.vdisplay = Xvfb(width=1200, height=800)
        world.vdisplay.start()

    world.browser = create_browser()

    yield

    world.browser.quit()
    delattr(world, 'browser')

    if hasattr(world, 'vdisplay'):
        world.vdisplay.stop()


def browser_type():
    """Browser type selected for the tests."""

    return os.environ.get('BROWSER_TYPE', 'chrome')


def chrome_builder():
    return webdriver.Chrome(os.path.join(NPM_BIN_DIR, 'chromedriver'))


def create_browser():
    """Create a Selenium browser for tests."""

    browsers = {
        'chrome': chrome_builder,
        'firefox': webdriver.Firefox,
        'phantomjs': webdriver.PhantomJS,
    }
    driver = browsers[browser_type()]

    return driver()
