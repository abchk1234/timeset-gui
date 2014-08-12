NAME = timeset-gui
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
docdir = /usr/share/$(NAME)
appdir = /usr/share/timeset-gui-$(VERSION)

all:

install: all
	$(INSTALL) -d $(DESTDIR)$(bindir)
	$(INSTALL) -d $(DESTDIR)$(icons)
	$(INSTALL) -d $(DESTDIR)$(deskdir)
	$(INSTALL) -d $(DESTDIR)$(docdir)
	$(INSTALL) -d $(DESTDIR)$(appdir)
	$(INSTALL) -m755 timeset-gui.py $(DESTDIR)$(bindir)/timeset-gui
	$(INSTALL) -m644 install/time-admin.png $(DESTDIR)$(icons)
	$(INSTALL) -m644 install/time-settings.desktop $(DESTDIR)$(deskdir)
	$(INSTALL) -m644 README.md $(DESTDIR)$(docdir)
	$(INSTALL) -m644 COPYING $(DESTDIR)$(docdir)
	$(INSTALL) -m644 makefile $(DESTDIR)$(appdir)
