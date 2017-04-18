""" Django Channels routing. """

import logging

from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route

from .consumers import TimeConsumer


logger = logging.getLogger(__name__)


class Demultiplexer(WebsocketDemultiplexer):
    """
    Demultiplex websocket communications.

    Consumers wired here should be based on `JsonWebsocketConsumer`.
    """

    http_user = True

    consumers = {
        "server_time": TimeConsumer,
    }


def reject_connection_consumer(message, *args, **kwargs):
    """Reject connection."""

    logger.info('Invalid request to path: %s', message['path'])

    message.reply_channel.send({"accept": False})


CHANNEL_ROUTING = [
    Demultiplexer.as_route(path=r'^/ws'),

    # Reject all connections that doesn't have a route defined.
    route("websocket.connect", reject_connection_consumer),
]
