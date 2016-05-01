#!/bin/env python3
#
# Mail Notify for dunst
#
# (c) 2016 Daniel Jankowski


import os
import re
import json
import imaplib


from gi.repository import Notify


CONFIG_PATH = '~/.mailnotifyrc'


def parse_config(path):
    if not os.path.exists(path):
        return False
    with open(path, 'r') as fp:
        return json.loads(fp.read())


def main():
    Notify.init("mail-notify")

    config = parse_config(os.path.expanduser(CONFIG_PATH))

    for account in config['accounts']:
        with imaplib.IMAP4_SSL(account['server']) as m:
            m.login(account['username'], account['password'])

            m.list()
            m.select('inbox')
            result, data = m.search(None, 'UNSEEN')
            count = len(data[0].decode('utf-8').split(' '))

            if data[0].decode('utf-8') == '':
                continue

            notification = Notify.Notification.new("Mail", "{count} new mail(s) at {address}".format(count=count, address=account['mail']), "dialog-information")
            notification.show()

            m.close()
            m.logout()
    pass


if __name__ == '__main__':
    main()
