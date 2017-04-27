from django.core import mail

from aloe import before, step

from channels_example.mail import MAIL_STORAGE
from channels_example.tools.persitentlist import PersistentList


@before.each_example
def link_persistent_outbox(*args, **kwargs):
    mail.outbox = PersistentList(MAIL_STORAGE)


@step(r'(\d+) emails? has been sent')
def mail_sent_count(self, count):
    expected = int(count)
    actual = len(mail.outbox)
    assert expected == actual, \
        "Expected to send {0} email(s), got {1}.".format(expected, actual)
