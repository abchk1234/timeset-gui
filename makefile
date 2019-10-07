NAME = timeset-gui
VERSION = 2.4
SHELL = /bin/bash
INSTALL = /usr/bin/install
MSGFMT = /usr/bin/msgfmt
SED = /bin/sed
DESTDIR =
bindir = /usr/bin
localedir = /usr/share/locale
icons = /usr/share/icons
deskdir = /usr/share/applications
mandir = /usr/share/man/man1
docdir = /usr/share/doc/$(NAME)
appdir = /usr/share/$(NAME)-$(VERSION)

all:
	cd po; make gettext

clean:
	rm po/*.mo

install: all
	$(INSTALL) -d $(DESTDIR)$(bindir)
	$(INSTALL) -d $(DESTDIR)$(icons)
	$(INSTALL) -d $(DESTDIR)$(deskdir)
	$(INSTALL) -d $(DESTDIR)$(docdir)
	$(INSTALL) -d $(DESTDIR)$(appdir)
	$(INSTALL) -m755 bin/$(NAME).py $(DESTDIR)$(bindir)/$(NAME)
	$(INSTALL) -m644 install/time-admin.png $(DESTDIR)$(icons)/$(NAME)-icon.png
	$(INSTALL) -m644 install/time-settings.desktop $(DESTDIR)$(deskdir)/$(NAME).desktop
	$(INSTALL) -m644 README.md $(DESTDIR)$(docdir)/README.md
	$(INSTALL) -m644 COPYING $(DESTDIR)$(docdir)/COPYING
	$(INSTALL) -m644 makefile $(DESTDIR)$(appdir)/makefile
	for file in mo/*.mo; \
	do \
		lang=$$(echo $$file | $(SED) -e 's#$(NAME)_##' -e 's#.*/\([^/]\+\).mo#\1#'); \
		$(INSTALL) -d $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES; \
		$(INSTALL) -m644 $$file  $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(NAME).mo; \
	done

uninstall:
	rm $(DESTDIR)$(bindir)/$(NAME)
	rm $(DESTDIR)$(icons)/$(NAME)-icon.png
	rm $(DESTDIR)$(deskdir)/$(NAME).desktop
	rm -r $(DESTDIR)$(docdir)
	rm -r $(DESTDIR)$(appdir)
	rm $(DESTDIR)/usr/share/locale/*/LC_MESSAGES/$(NAME).mo
