import os
import shelve

from django.core.mail.backends.base import BaseEmailBackend


MAIL_STORAGE = '.mail_storage'
OUTBOX = 'outbox'


class EmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super(EmailBackend, self).__init__(*args, **kwargs)

        # Clean outbox.
        try:
            os.remove(MAIL_STORAGE)
        except OSError:
            pass

    def send_messages(self, messages):
        """Redirect messages to the dummy outbox"""
        msg_count = 0

        for message in messages:  # .message() triggers header validation
            message.message()

            storage = shelve.open(MAIL_STORAGE)
            outbox = storage.get(OUTBOX, [])
            outbox.append(message)
            storage[OUTBOX] = outbox
            storage.close()

            msg_count += 1

        return msg_count
