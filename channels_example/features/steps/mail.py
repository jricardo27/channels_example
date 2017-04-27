from django.core import mail

from aloe import step


@step(r'(\d+) emails? has been sent')
def mail_sent_count(self, count):
    expected = int(count)
    actual = len(mail.outbox)
    assert expected == actual, \
        "Expected to send {0} email(s), got {1}.".format(expected, actual)
