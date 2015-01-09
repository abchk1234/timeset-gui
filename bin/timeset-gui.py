#!/usr/bin/python2
##
#  timeset-gui - A GUI to manage system date and time
#  Copyright (C) 2013-2015 Aaditya Bagga <aaditya_gnulinux@zoho.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#  This program is distributed WITHOUT ANY WARRANTY;
#  without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

import shlex
import subprocess
from gi.repository import Gtk
import os.path

program_icon = "/usr/share/icons/timeset-gui-icon.png"
APP_NAME = "timeset-gui"

# i18n (Internationalization)
import gettext
gettext.bindtextdomain(APP_NAME, '/usr/share/locale')
gettext.textdomain(APP_NAME)
_ = gettext.gettext

# l18n (Localization)
gettext.install('timeset-gui')

# Common strings
msg_warn = _('Warning!')

# Checking for systemd
def is_systemd():
    if os.path.exists('/usr/bin/timedatectl') and not subprocess.call(["pidof", "systemd"]):
        # not subprocess.call used as it returns 0 on success
        return 1
    else:
        return 0

def is_openrc():
    if os.path.exists('/run/openrc'):
        return 1
    else:
        return 0

class on_show_current_date_and_time:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_title(_("Current date and time"))
        viewbox = Gtk.TextView()
        viewbox.set_property('editable', False)
        viewbox.set_cursor_visible(False)
        viewbox.set_border_width(10)
        window2.add(viewbox)
        textbuffer = viewbox.get_buffer()
        if is_systemd():
            sp = subprocess.Popen(shlex.split('timedatectl status'), stdout=subprocess.PIPE)
        else:
            sp = subprocess.Popen(shlex.split('date'), stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("{0}".format(out))
        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class on_show_timezones:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_default_size(300, 400)
        window2.set_title(_("Known timezones"))
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        window2.add(scrolledwindow)
        viewbox = Gtk.TextView()
        viewbox.set_property('editable', False)
        viewbox.set_cursor_visible(False)
        viewbox.set_border_width(10)
        scrolledwindow.add(viewbox)
        textbuffer = viewbox.get_buffer()
        if is_systemd():
            sp = subprocess.Popen(shlex.split('timedatectl list-timezones'), stdout=subprocess.PIPE)
        else:
            p1 = subprocess.Popen(shlex.split('find -L /usr/share/zoneinfo/posix -mindepth 2 -type f -printf "%P\n"'), stdout=subprocess.PIPE)
            sp = subprocess.Popen(["sort"], stdin=p1.stdout, stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("{0}".format(out))

        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class set_timezone(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, _("Set system timezone"), parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label(_('Enter the timezone. It should be like \nContinent/City - Europe/Berlin'))
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class set_ntp_at_statup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, _("Enable or disable NTP"), parent,
            Gtk.DialogFlags.MODAL, buttons=(_("Enable"), Gtk.ResponseType.OK, _("Disable"), Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label(_('Enable or disable NTP usage.\nNTP stands for Network Time Protocol.\nIf NTP is enabled the system will periodically\nsynchronize time from the network.'))
        box.add(label)
        self.show_all()

class control_the_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, _("Control the hardware clock"), parent,
            Gtk.DialogFlags.MODAL, buttons=(_("UTC"), Gtk.ResponseType.OK, _("Local time"), Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label(_('Set the hardware clock to use'))
        box.add(label)
        self.show_all()

class on_read_time_from_hw_clock:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_title(_("Hardware clock time"))
        viewbox = Gtk.TextView()
        viewbox.set_property('editable', False)
        viewbox.set_cursor_visible(False)
        viewbox.set_border_width(10)
        window2.add(viewbox)
        textbuffer = viewbox.get_buffer()
        sp = subprocess.Popen(shlex.split('/sbin/hwclock -D'), stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("{0}".format(out))
        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class sync_system_time_from_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, _("Synchronize system time from hardware clock"), parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label(_('Synchronize system time from the hardware clock.\nClick OK and wait a few moments while the time is being synchronised.\n'))
        box.add(label)
        self.show_all()

class set_time_manually(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, _("Set system time"), parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label(_('Enter the time. The time may be formatted\nlike this: 2013-11-18 09:12:45\nor just yyyy-mm-dd hh:mm'))
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class MainWindow(Gtk.Window):
    def on_sync_system_time_from_hw_clock(self, widget):
        sp = subprocess.Popen(shlex.split("/sbin/hwclock -s"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, msg_warn)
            dialog2.format_secondary_text("{0}".format(err))
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "System time synchronized to hardware clock!")
            dialog2.format_secondary_text("{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def on_sync_hw_clock_to_system_time(self, widget):
        sp = subprocess.Popen(shlex.split("/sbin/hwclock -w"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, msg_warn)
            dialog2.format_secondary_text("{0}".format(err))
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, _("Hardware clock synchronized to system time!"))
            dialog2.format_secondary_text("{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def on_control_the_hw_clock(self, widget):
        dialog = control_the_hw_clock(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if is_systemd():
                sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            elif is_openrc():
                if os.path.isfile('/etc/conf.d/hwclock'):
                    sp = subprocess.Popen(shlex.split('sed -i "s/clock=.*/clock=\"UTC\"/" /etc/conf.d/hwclock'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                    subprocess.Popen(shlex.split('/sbin/hwclock --systohc --utc'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    sp = subprocess.Popen(shlex.split('/sbin/hwclock --systohc --utc'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
            else:
                    sp = subprocess.Popen(shlex.split('/sbin/hwclock --systohc --utc'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, _("Hardware clock set to UTC!"))
                dialog2.run()
                dialog2.destroy()
        if response == Gtk.ResponseType.CANCEL:
            if is_systemd():
                sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            elif is_openrc():
                if os.path.isfile('/etc/conf.d/hwclock'):
                    sp = subprocess.Popen(shlex.split('sed -i "s/clock=.*/clock=\"local\"/" /etc/conf.d/hwclock'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                    subprocess.Popen(shlex.split('/sbin/hwclock --systohc --localtime'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    sp = subprocess.Popen(shlex.split('/sbin/hwclock --systohc --localtime'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
            else:
                    sp = subprocess.Popen(shlex.split('/sbin/hwclock --systohc --localtime'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, _("Hardware clock set to local time!"))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_set_ntp_at_statup(self, widget):
        dialog = set_ntp_at_statup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            if is_systemd():
                sp = subprocess.Popen(shlex.split('timedatectl set-ntp 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            elif is_openrc():
                if os.path.isfile('/etc/init.d/ntpd'):
                    sp = subprocess.Popen(shlex.split('rc-update add ntpd'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                else:
                    err = _('ntpd service not found')
            else:
                err = _('For this to work ntpd needs to be present.\nFurthur you may need need to edit /etc/ntp.conf (or similar) file, and then enable the ntp daemon to start at boot.\nThis feature is not handled by this program.')
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, _("NTP enabled!"))
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        if response == Gtk.ResponseType.CANCEL:
            if is_systemd():
                sp = subprocess.Popen(shlex.split('timedatectl set-ntp 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            elif is_openrc():
                if os.path.isfile('/etc/init.d/ntpd'):
                    sp = subprocess.Popen(shlex.split('rc-update del ntpd'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                else:
                    err = _('ntpd service not found')
            else:
                err = _('For this to work ntpd needs to be present.\nFurthur you may need need to edit /etc/ntp.conf (or similar) file, and then enable the ntp daemon to start at boot.\nThis feature is not handled by this program.')
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, _("NTP disabled!"))
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_sync_from_network(self, widget):
        if os.path.exists('/usr/sbin/ntpdate'):
            sp = subprocess.Popen(shlex.split("/usr/sbin/ntpdate -u 0.pool.ntp.org"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
        else:
            err = _('Could not find ntpdate')
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, msg_warn)
            dialog2.format_secondary_text("{0}".format(err))
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, _("Success! Time updated."))
            dialog2.format_secondary_text("{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def read_time_from_hw_clock(self, widget):
        on_read_time_from_hw_clock()

    def show_timezones(self, widget):
        on_show_timezones()

    def show_current_date_and_time(self, widget):
        on_show_current_date_and_time()

    def on_set_timezones(self, widget):
        dialog = set_timezone(self)
        response = dialog.run()
        entered_text = dialog.entry.get_text()
        if response == Gtk.ResponseType.OK:
            if is_systemd():
                sp = subprocess.Popen(shlex.split("timedatectl set-timezone {0}".format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            else:
                if os.path.isfile('/usr/share/zoneinfo/posix/{0}'.format(entered_text)):
                    sp = subprocess.Popen(shlex.split("ln -sf /usr/share/zoneinfo/posix/{0} /etc/localtime".format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                else:
                    err = _('Invalid timezone')
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, _("Timezone changed!"))
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_set_time_manually(self, widget):
        dialog = set_time_manually(self)
        response = dialog.run()
        entered_text = dialog.entry.get_text()
        if response == Gtk.ResponseType.OK:
            if is_systemd():
                sp = subprocess.Popen(shlex.split("timedatectl set-time '%s'" % entered_text), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
            else:
                import re
                p1 = re.match("[0-9]*:[0-9]*", "%s" % entered_text) # time, like hh:mm
                p2 = re.match("[0-9]*-[0-9]*-[0-9]*", "%s" % entered_text) # date, like yyyy-mm-dd
                p3 = re.match("[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*", "%s" % entered_text) # date and time
                p4 = re.match("[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*", "%s" % entered_text) # date and time with seconds
		if p1 or p2 or p3 or p4:
                    sp = subprocess.Popen(shlex.split("date -s '%s'" % entered_text), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = sp.communicate()
                else:
                    err = _('Time not entered correctly.')
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, msg_warn)
                dialog2.format_secondary_text("{0}".format(err))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, _("Time changed!"))
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()


    def __init__(self):
        Gtk.Window.__init__(self, title=_("TimeSet - Manage system date and time"))

        if os.path.isfile(program_icon):
            self.set_icon_from_file(program_icon)

        self.set_border_width(6)
        self.set_size_request(320, 300)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        self.add(vbox)

        grid = Gtk.Grid()
        grid.set_row_spacing(1)
        grid.set_column_spacing(1)
        vbox.add(grid)

        label = Gtk.Label(label=_(" 1. Show current date and time"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 1, 1, 1)
        self.button_1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button_1.set_tooltip_text(_("Show current date and time configuration"))
        self.button_1.connect("clicked", self.show_current_date_and_time)
        grid.attach(self.button_1, Gtk.PositionType.RIGHT, 1, 1, 1)

        label = Gtk.Label(label=_(" 2. Show timezones"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 2, 1, 1)
        self.button_2 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button_2.set_tooltip_text(_("Show known timezones"))
        self.button_2.connect("clicked", self.show_timezones)
        grid.attach(self.button_2, Gtk.PositionType.RIGHT, 2, 1, 1)

        label = Gtk.Label(label=_(" 3. Set system timezone"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 3, 1, 1)
        self.button_3 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_3.set_tooltip_text(_("Set system timezone"))
        self.button_3.connect("clicked", self.on_set_timezones)
        grid.attach(self.button_3, Gtk.PositionType.RIGHT, 3, 1, 1)

        label = Gtk.Label(label=_(" 4. Synchronize time from the network"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 4, 1, 1)
        self.button_4 = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_4.set_tooltip_text(_("Synchronize time from the network using NTP"))
        self.button_4.connect("clicked", self.on_sync_from_network)
        grid.attach(self.button_4, Gtk.PositionType.RIGHT, 4, 1, 1)

        label = Gtk.Label(label=_(" 5. Choose whether NTP is enabled"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 5, 1, 1)
        self.button_5 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_5.set_tooltip_text(_("Choose whether NTP (Network Time Protocol) is enabled"))
        self.button_5.connect("clicked", self.on_set_ntp_at_statup)
        grid.attach(self.button_5, Gtk.PositionType.RIGHT, 5, 1, 1)

        label = Gtk.Label(label=_(" 6. Hardware clock in UTC or local time"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 6, 1, 1)
        self.button_6 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_6.connect("clicked", self.on_control_the_hw_clock)
        self.button_6.set_tooltip_text(_("Control whether the hardware clock is in UTC or local time"))
        grid.attach(self.button_6, Gtk.PositionType.RIGHT, 6, 1, 1)

        label = Gtk.Label(label=_(" 7. Read time from the hardware clock"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 7, 1, 1)
        self.button_7 = Gtk.ToolButton(stock_id=Gtk.STOCK_ABOUT)
        self.button_7.set_tooltip_text(_("Read time from the hardware clock"))
        self.button_7.connect("clicked", self.read_time_from_hw_clock)
        grid.attach(self.button_7, Gtk.PositionType.RIGHT, 7, 1, 1)

        label = Gtk.Label(label=_(" 8. Synchronize hardware clock to system time"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 8, 1, 1)
        self.button_8 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_8.set_tooltip_text(_("Synchronize hardware clock to system time"))
        self.button_8.connect("clicked", self.on_sync_hw_clock_to_system_time)
        grid.attach(self.button_8, Gtk.PositionType.RIGHT, 8, 1, 1)

        label = Gtk.Label(label=_(" 9. Synchronize system time to hardware clock"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 9, 1, 1)
        self.button_9 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_9.set_tooltip_text(_("Synchronize system time to hardware clock time"))
        self.button_9.connect("clicked", self.on_sync_system_time_from_hw_clock)
        grid.attach(self.button_9, Gtk.PositionType.RIGHT, 9, 1, 1)

        label = Gtk.Label(label=_("10. Adjust the date and time manually"))
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 10, 1, 1)
        self.button_10 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_10.set_tooltip_text(_("Set the date and time manually"))
        self.button_10.connect("clicked", self.on_set_time_manually)
        grid.attach(self.button_10, Gtk.PositionType.RIGHT, 10, 1, 1)


if __name__ == '__main__':
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
