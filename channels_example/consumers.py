""" Django channel consumers. """

import datetime
import logging

from channels.generic.websockets import JsonWebsocketConsumer, WebsocketMultiplexer

logger = logging.getLogger(__name__)


class TimeConsumer(JsonWebsocketConsumer):
    """A consumer to serve the server time."""

    time_group = 'time_group'
    groups = [time_group]
    stream = 'server_time'
    date_format = '%Y-%m-%d %H:%M:%S.%f'

    def receive(self, content, multiplexer, **kwargs):
        """Process messages from the client to this stream."""

        logger.info('Message received: %s', str(content))

        if content['action'] == 'get_time':
            message = {
                'serverTime': datetime.datetime.now().strftime(
                    self.date_format,
                ),
            }
            self.time_group_send(message)
        else:
            multiplexer.send("Invalid action.")

    @classmethod
    def time_group_send(cls, content):
        """Send messages to the time group."""

        WebsocketMultiplexer.group_send(cls.time_group, cls.stream, content)
