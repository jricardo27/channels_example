import shelve

from aloe import step

from channels_example.mail import MAIL_STORAGE, OUTBOX


@step(r'(\d+) emails? has been sent')
def mail_sent_count(self, count):

    storage = shelve.open(MAIL_STORAGE)
    outbox = storage[OUTBOX]
    storage.close()

    expected = int(count)
    actual = len(outbox)
    assert expected == actual, \
        "Expected to send {0} email(s), got {1}.".format(expected, actual)
