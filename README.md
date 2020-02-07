# Goto

This is a local bookmarks server.

## Setup

* Install pipenv
* Add `127.0.0.1	go` to your /etc/hosts
* Add the `goto` directory to your path (so the `bookmark` CLI works).
* Start `sudo make serve`. This will create a sqlite db containing your bookmarks and start the webserver.
* Add a bookmark using the cli, e.g. `bookmark add goto-gh https://github.com/lucaswiman/goto`
* Direct your browser to http://go/goto-gh which should redirect you here. Note the "http" part is important, since many modern browsers will attempt https first. In the future, you can type go/<name> to go to your tagged bookmark.

## Warnings

* You should ensure that port 80 is not exposed or others on the same network could access your bookmarks.
* The bookmarks database is just saved to the filesystem, so may be lost easily.
