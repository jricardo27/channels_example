import pytz

from datetime import datetime
from django.conf import settings
from freezegun import freeze_time
from aloe import after, step, world


def unmock_time():
    """Stop mocking date, if active."""

    try:
        world.freezer.stop()
        delattr(world, 'freezer')
    except AttributeError:
        pass


@step(r'Today\'s date is (\d{4}-\d{2}-\d{2})'
      r'(?: and time is (\d{,2}):(\d{2})h)?')
def mock_time(self, datestr, hour, minute):
    """
    Mock today's date.

    :param self: Object reference to aloe. [Not used].
    :param datestr: String representing the new date in the format YYYY-MM-DD.
    :param hour: Number representing the new time in 24h format. [Optional]
    :param minute: Number representing the new time. Between 0 and 59.
        [Optional, but required if the `hour` is specified.
    """

    unmock_time()

    current_timezone = settings.TIME_ZONE

    mocked_time = datetime.strptime(datestr, '%Y-%m-%d')

    if hour and minute:
        mocked_time = mocked_time.replace(hour=int(hour), minute=int(minute))

    # Localize datetime to current timezone.
    mocked_time = (
        pytz.timezone(current_timezone).localize(mocked_time)
    )

    world.freezer = freeze_time(mocked_time, ignore=[
        'aloe_webdriver',
    ])
    world.freezer.start()


@after.each_example
def unfreeze_time(*args):
    """Stop mocking time."""

    unmock_time()
