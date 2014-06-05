VERSION = 1.8
SHELL = /bin/bash
INSTALL = /usr/bin/install
MSGFMT = /usr/bin/msgfmt
SED = /bin/sed
DESTDIR =
bindir = /usr/bin
localedir = /usr/share/locale
icons = /usr/share/icons
deskdir = /usr/share/applications
mandir = /usr/share/man/man1/
appdir = /usr/share/timeset-gui-$(VERSION)

all:

install: all
	$(INSTALL) -d $(DESTDIR)$(bindir)
	$(INSTALL) -d $(DESTDIR)$(icons)
	$(INSTALL) -d $(DESTDIR)$(deskdir)
	$(INSTALL) -d $(DESTDIR)$(appdir)
	$(INSTALL) -m755 timeset-gui.py $(DESTDIR)$(bindir)/timeset-gui
	$(INSTALL) -m644 time-admin.png $(DESTDIR)$(icons)
	$(INSTALL) -m644 TimeSettings.desktop $(DESTDIR)$(deskdir)
	$(INSTALL) -m644 README.md $(DESTDIR)$(appdir)
	$(INSTALL) -m644 COPYING $(DESTDIR)$(appdir)
	$(INSTALL) -m644 makefile $(DESTDIR)$(appdir)
