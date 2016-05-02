#!/usr/bin/env python3
#
# Mail Notify for dunst
#
# (c) 2016 Daniel Jankowski


import os
import json
import imaplib


from gi.repository import Notify
from threading import Thread, Event


CONFIG_PATH = '~/.mailnotifyrc'


class MailThread(Thread):

    def __init__(self, accounts, interval):
        super().__init__()
        self.stop_event = Event()
    
        # Mail attributes.
        self.__accounts = accounts
        self.__interval = interval * 60.0

    def run(self):
        while not self.stop_event.is_set():
            for account in self.__accounts:
                # Try to connect to the imap server.
                try:
                    with imaplib.IMAP4_SSL(account['server']) as m:
                        # Try to login.
                        try:
                            m.login(account['username'], account['password'])
                        except Exception as e:
                            continue

                        # Get number and ids of unread mails.
                        m.select('inbox')
                        result, data = m.search(None, 'UNSEEN')

                        if result == 'OK':
                            # Get count of unread mails
                            count = len(data[0].decode('utf-8').split(' '))

                            if data[0].decode('utf-8') == '':
                                continue

                            # Print notification with libnotify.
                            notification = Notify.Notification.new("Mail", "{count} new mail(s) at {address}".format(count=count, address=account['mail']), "dialog-information")
                            notification.show()

                        # Close connection to imap server
                        m.close()
                        m.logout()
                except Exception as e:
                    continue
            self.stop_event.wait(60.0)


def parse_config(path):
    # Check if config exists.
    if not os.path.exists(path):
        return False

    # Read config and auto validate for json.
    with open(path, 'r') as fp:
        return json.loads(fp.read())


def main():
    # Initialize connection to libnotify.
    Notify.init("mail-notify")

    # Get config parameters.
    config = parse_config(os.path.expanduser(CONFIG_PATH))

    # If config not exists, return.
    if not config:
        print('Error: No config file found.')
        return -1

    # Start mail thread.
    mail_thread = MailThread(config['accounts'], config['interval'])
    mail_thread.start()
    pass


if __name__ == '__main__':
    main()
