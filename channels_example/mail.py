from django.core import mail
from django.core.mail.backends.locmem import EmailBackend as LocMemBackend

from channels_example.tools.persitentlist import PersistentList

MAIL_STORAGE = '.mail_storage'

class EmailBackend(LocMemBackend):
    def __init__(self, *args, **kwargs):
        super(EmailBackend, self).__init__(*args, **kwargs)

        if (not hasattr(mail, 'outbox') or
                not isinstance(mail.outbox, PersistentList)):
            mail.outbox = PersistentList(MAIL_STORAGE, clear_file=True)
