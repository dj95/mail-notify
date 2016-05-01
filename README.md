# Mailnotify

A simple mail notifier, which show the count of unread
mails with libnotify for imap accounts.

### Requirements

- Python 3
- Python 3 modules:
    - imaplib
    - gi.repository
- libnotify

*And its dependencies...*


### Installation

- Clone this repo to `/opt/`
- Copy the `mailnotifyrc` from `conf/` to `~/.mailnotifyrc`
- Copy the systemd-timer and the relating systemd-user-service from `systemd/` to `.config/systemd/user/`
- Reload your user-services with `systemctl --user daemon-reload`
- Start the service with `systemctl --user start mail-notify`
- *Optional:* To start the systemd service at the beginning of your user session, enable it
    with `systemctl --user enable mail-notify`


### License

MIT/X Consortium License

© 2016 Daniel Jankowski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
