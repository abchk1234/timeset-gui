#!/usr/bin/python
import shlex
import subprocess
from gi.repository import Gtk, Gdk

program_icon = "/home/frost/Desktop/time-admin.png"

class on_read_time_from_hw_clock:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_title("Hardware Clock Time")
        viewbox = Gtk.TextView()
        viewbox.set_property('editable', False)
        viewbox.set_cursor_visible(False)
        viewbox.set_border_width(10)
        window2.add(viewbox)
        textbuffer = viewbox.get_buffer()
        sp = subprocess.Popen(shlex.split('hwclock -D'), stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("%s" % out)

        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class on_show_current_date_and_time:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_title("Current date and time")
        viewbox = Gtk.TextView()
        viewbox.set_property('editable', False)
        viewbox.set_cursor_visible(False)
        viewbox.set_border_width(10)
        window2.add(viewbox)
        textbuffer = viewbox.get_buffer()
        sp = subprocess.Popen(shlex.split('timedatectl status'), stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("%s" % out)

        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class on_show_timezones:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_default_size(300, 400)
        window2.set_title("Known timezones")
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
        sp = subprocess.Popen(shlex.split('timedatectl list-timezones'), stdout=subprocess.PIPE)
        out, err = sp.communicate()
        textbuffer.set_text("%s" % out)

        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class sync_system_time_from_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Sync system time from HW clock", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Synchronize System Time from Hardware Clock.\nClick OK and wait a few moments while the time is being synchronised\n')
        box.add(label)
        self.show_all()

class sync_hw_clock_to_system_time(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Sync HW clock to system time", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Synchronize Hardware Clock to System Time.\nClick OK and wait a few moments while the time is being synchronised\n')
        box.add(label)
        self.show_all()

class control_the_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set time", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enter 0 to set Hardware clock to UTC\nand 1 to set it to Local time')
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class disable_ntp_at_startup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Disable NTP at startup", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Click OK if you want to disable NTP at system startup\n')
        box.add(label)
        self.show_all()

class enable_ntp_at_startup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable NTP at startup", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Click OK if you want to enable NTP at system startup\n')
        box.add(label)
        self.show_all()

class set_ntp_at_statup(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable & disalbe ntp", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enter 1 to enable NTP and 0 to disable NTP')
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class sync_from_network(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Synchronize time from network", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('NTP should be installed for this to work.\nClick OK and wait a few moments while the time is being synchronised\nYou will get the result wheter the synchronization was successful or not\nIf the field is empty it means:\nCan\'t adjust the time of day: Operation not permitted')
        box.add(label)
        self.show_all()

class set_timezone(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set timezone", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enter the TimeZone. It should be like \nContinent/City "Europe/Berlin"')
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class set_time_manually(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set time", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enter the time. The time may be specified\nin the format "2013-11-18 09:12:45"')
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class MainWindow(Gtk.Window):

    def on_sync_system_time_from_hw_clock(self, widget):
        dialog = sync_system_time_from_hw_clock(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('hwclock -s'), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_sync_hw_clock_to_system_time(self, widget):
        dialog = sync_hw_clock_to_system_time(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('hwclock -w'), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_control_the_hw_clock(self, widget):
        dialog = control_the_hw_clock(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc %s' % dialog.entry.get_text()), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_disable_ntp_at_startup(self, widget):
        dialog = disable_ntp_at_startup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('systemctl disable ntpd'), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_enable_ntp_at_startup(self, widget):
        dialog = enable_ntp_at_startup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('systemctl enable ntpd'), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_set_ntp_at_statup(self, widget):
        dialog = set_ntp_at_statup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-ntp %s' % dialog.entry.get_text()), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_sync_from_network(self, widget):
        dialog = sync_from_network(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            class start_sync:
                def __init__(self):
                    window2 = Gtk.Window()
                    window2.set_default_size(650, 70)
                    window2.set_title("The result:")
                    scrolledwindow = Gtk.ScrolledWindow()
                    scrolledwindow.set_hexpand(True)
                    scrolledwindow.set_vexpand(True)
                    window2.add(scrolledwindow)
                    viewbox = Gtk.TextView()
                    viewbox.set_property('editable', False)
                    viewbox.set_cursor_visible(False)
                    viewbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
                    viewbox.set_border_width(10)
                    scrolledwindow.add(viewbox)
                    textbuffer = viewbox.get_buffer()
                    sp = subprocess.Popen(shlex.split('ntpdate -u pool.ntp.org'), stdout=subprocess.PIPE)
                    out, err = sp.communicate()
                    textbuffer.set_text("%s" % out)

                    window2.connect("destroy", lambda q: Gtk.main_quit())
                    window2.show_all()
                    Gtk.main()
            dialog.destroy()
            start_sync()

    def read_time_from_hw_clock(self, widget):
        on_read_time_from_hw_clock()

    def show_timezones(self, widget):
        on_show_timezones()

    def show_current_date_and_time(self, widget):
        on_show_current_date_and_time()

    def on_set_timezones(self, widget):
        dialog = set_timezone(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-timezone %s' % dialog.entry.get_text()), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_set_time_manually(self, widget):
        dialog = set_time_manually(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-time %s' % dialog.entry.get_text()), stdout=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def __init__(self):
        Gtk.Window.__init__(self, title="TimeSet")

        self.set_icon_from_file(program_icon)
        self.set_border_width(6)
        self.set_size_request(200, 20)
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        grid = Gtk.Grid()
        grid.set_row_spacing(7)
        grid.set_column_spacing(13)
        vbox.add(grid)

        label = Gtk.Label(label="1. Current Date and Time")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 1, 1, 1)

        self.button1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button1.set_tooltip_text("Show Current Date and Time Configuration")
        self.button1.connect("clicked", self.show_current_date_and_time)
        grid.attach(self.button1, Gtk.PositionType.LEFT, 2, 1, 1)

        label = Gtk.Label(label="2. Known Timezones")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 1, 1, 1)

        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button_about.set_tooltip_text("Show Known Timezones")
        self.button_about.connect("clicked", self.show_timezones)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 2, 1, 1)

        label = Gtk.Label(label="3. Set System Timezone")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 3, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_about.set_tooltip_text("Set System Timezone")
        self.button_about.connect("clicked", self.on_set_timezones)
        grid.attach(self.button_about, Gtk.PositionType.LEFT, 4, 1, 1)

        label = Gtk.Label(label="4. Synchronize Time")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 3, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize Time from the Network")
        self.button_about.connect("clicked", self.on_sync_from_network)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 4, 1, 1)

        label = Gtk.Label(label="5. Control NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 5, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.set_tooltip_text("Control whether NTP is used or not")
        self.button_about.connect("clicked", self.on_set_ntp_at_statup)
        grid.attach(self.button_about, Gtk.PositionType.LEFT, 6, 1, 1)

        label = Gtk.Label(label="6. Enable NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 5, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_about.set_tooltip_text("Enable NTP at Startup")
        self.button_about.connect("clicked", self.on_enable_ntp_at_startup)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 6, 1, 1)

        label = Gtk.Label(label="7. Disable NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 7, 1, 1)

        self.button1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DELETE)
        self.button1.set_tooltip_text("Disable NTP at Startup")
        self.button1.connect("clicked", self.on_disable_ntp_at_startup)
        grid.attach(self.button1, Gtk.PositionType.LEFT, 8, 1, 1)

        label = Gtk.Label(label="8. Control the HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 7, 1, 1)

        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.connect("clicked", self.on_control_the_hw_clock)
        self.button_about.set_tooltip_text("Control whether Hardware Clock is in Local Time or not")
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 8, 1, 1)

        label = Gtk.Label(label="9. Read time from HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 9, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_ABOUT)
        self.button_about.set_tooltip_text("Read the time from the Hardware Clock")
        self.button_about.connect("clicked", self.read_time_from_hw_clock)
        grid.attach(self.button_about, Gtk.PositionType.LEFT, 10, 1, 1)

        label = Gtk.Label(label="10. Synchronize HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 9, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize Hardware Clock to System Time")
        self.button_about.connect("clicked", self.on_sync_hw_clock_to_system_time)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 10, 1, 1)

        label = Gtk.Label(label="11. Synchronize Time 2")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 11, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize System Time from Hardware Clock")
        self.button_about.connect("clicked", self.on_sync_system_time_from_hw_clock)
        grid.attach(self.button_about, Gtk.PositionType.LEFT, 12, 1, 1)

        label = Gtk.Label(label="12. Set Time manually")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        grid.attach(label, Gtk.PositionType.RIGHT, 11, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.set_tooltip_text("Set System Time manually")
        self.button_about.connect("clicked", self.on_set_time_manually)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 12, 1, 1)

if __name__ == '__main__':
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()