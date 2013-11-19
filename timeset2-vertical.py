#!/usr/bin/python
import shlex
import subprocess
from gi.repository import Gtk, Gdk

program_icon = "/usr/share/icons/time-admin.png"

class on_read_time_from_hw_clock:
    def __init__(self):
        window2 = Gtk.Window()
        window2.set_title("Hardware Clock Time")
        viewbox = Gtk.TextView()
        viewbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        viewbox.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
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
        viewbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        viewbox.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
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
        viewbox.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        viewbox.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
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

class control_the_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Control the HW clock", parent,
            Gtk.DialogFlags.MODAL, buttons=("UTC", Gtk.ResponseType.OK, "Local time", Gtk.ResponseType.CANCEL))
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
        box = self.get_content_area()
        label = Gtk.Label('Adjust the Hardware clock to:\n')
        box.add(label)
        self.show_all()

class disable_ntp_at_startup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Disable NTP at startup", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
        box = self.get_content_area()
        label = Gtk.Label('Click OK if you want to disable NTP at system startup\n')
        box.add(label)
        self.show_all()

class enable_ntp_at_startup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable NTP at startup", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
        box = self.get_content_area()
        label = Gtk.Label('Click OK if you want to enable NTP at system startup\n')
        box.add(label)
        self.show_all()

class set_ntp_at_statup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable & disable ntp", parent,
            Gtk.DialogFlags.MODAL, buttons=("Enable", Gtk.ResponseType.OK, "Disable", Gtk.ResponseType.CANCEL))
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
        box = self.get_content_area()
        label = Gtk.Label('Enable or Disable NTP at system startup\n')
        box.add(label)
        self.show_all()

class set_timezone(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set timezone", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
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
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
        box = self.get_content_area()
        label = Gtk.Label('Enter the time. The time may be specified\nin the format "2013-11-18 09:12:45"')
        box.add(label)
        self.entry = Gtk.Entry()
        box.add(self.entry)
        self.show_all()

class MainWindow(Gtk.Window):

    def on_sync_system_time_from_hw_clock(self, widget):
        sp = subprocess.Popen(shlex.split("hwclock -s"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Warning !")
            dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
            dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
            dialog2.format_secondary_text(
                "{0}".format(err))
            dialog2.run()
            dialog2.destroy()

    def on_sync_hw_clock_to_system_time(self, widget):
        sp = subprocess.Popen(shlex.split("hwclock -w"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Warning !")
            dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
            dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
            dialog2.format_secondary_text(
                "{0}".format(err))
            dialog2.run()
            dialog2.destroy()

    def on_control_the_hw_clock(self, widget):
        dialog = control_the_hw_clock(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
        if response == Gtk.ResponseType.CANCEL:
            sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_disable_ntp_at_startup(self, widget):
        dialog = disable_ntp_at_startup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('systemctl disable ntpd'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err_disable_ntp = sp.communicate()
            if err_disable_ntp:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning !")
                dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
                dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
                dialog2.format_secondary_text(
                    "{0}".format(err_disable_ntp))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_enable_ntp_at_startup(self, widget):
        dialog = enable_ntp_at_startup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('systemctl enable ntpd'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err_enable_ntp = sp.communicate()
            if err_enable_ntp:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning !")
                dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
                dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
                dialog2.format_secondary_text(
                    "{0}".format(err_enable_ntp))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_set_ntp_at_statup(self, widget):
        dialog = set_ntp_at_statup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-ntp 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
        if response == Gtk.ResponseType.CANCEL:
            sp = subprocess.Popen(shlex.split('timedatectl set-ntp 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
        dialog.destroy()

    def on_sync_from_network(self, widget):
        sp = subprocess.Popen(shlex.split("ntpdate -u pool.ntp.org"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Warning !")
            dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
            dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
            dialog2.format_secondary_text(
                "Cannot synchronize from the network right now.\nMake sure that you are running this program as root and try again.")
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
            sp = subprocess.Popen(shlex.split("timedatectl set-timezone {0}".format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning !")
                dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
                dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
                dialog2.format_secondary_text(
                    "{0} is not a valid timezone".format(entered_text))
                dialog2.run()
                dialog2.destroy()
            dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

    def on_set_time_manually(self, widget):
        dialog = set_time_manually(self)
        response = dialog.run()
        entered_text = dialog.entry.get_text()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split("timedatectl set-time {0}".format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning !")
                dialog2.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
                dialog2.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 0, 1, 1))
                dialog2.format_secondary_text(
                    "{0} is not a valid time".format(entered_text))
                dialog2.run()
                dialog2.destroy()
            dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

    def __init__(self):
        Gtk.Window.__init__(self, title="TimeSet")

        self.set_icon_from_file(program_icon)
        self.set_border_width(6)
        self.set_size_request(200, 20)
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 1))
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        grid = Gtk.Grid()
        grid.set_row_spacing(3)
        grid.set_column_spacing(5)
        vbox.add(grid)

        label = Gtk.Label(label="1. Current Date and Time")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 1, 1, 1)

        self.button1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button1.set_tooltip_text("Show Current Date and Time Configuration")
        self.button1.connect("clicked", self.show_current_date_and_time)
        grid.attach(self.button1, Gtk.PositionType.RIGHT, 1, 1, 1)

        label = Gtk.Label(label="2. Known Timezones")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 2, 1, 1)

        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button_about.set_tooltip_text("Show Known Timezones")
        self.button_about.connect("clicked", self.show_timezones)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 2, 1, 1)

        label = Gtk.Label(label="3. Set System Timezone")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 3, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_about.set_tooltip_text("Set System Timezone")
        self.button_about.connect("clicked", self.on_set_timezones)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 3, 1, 1)

        label = Gtk.Label(label="4. Synchronize Time")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 4, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize Time from the Network")
        self.button_about.connect("clicked", self.on_sync_from_network)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 4, 1, 1)

        label = Gtk.Label(label="5. Control NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 5, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.set_tooltip_text("Control whether NTP is used or not")
        self.button_about.connect("clicked", self.on_set_ntp_at_statup)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 5, 1, 1)

        label = Gtk.Label(label="6. Enable NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 6, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_about.set_tooltip_text("Enable NTP at Startup")
        self.button_about.connect("clicked", self.on_enable_ntp_at_startup)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 6, 1, 1)

        label = Gtk.Label(label="7. Disable NTP")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 7, 1, 1)

        self.button1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DELETE)
        self.button1.set_tooltip_text("Disable NTP at Startup")
        self.button1.connect("clicked", self.on_disable_ntp_at_startup)
        grid.attach(self.button1, Gtk.PositionType.RIGHT, 7, 1, 1)

        label = Gtk.Label(label="8. Control the HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 8, 1, 1)

        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.connect("clicked", self.on_control_the_hw_clock)
        self.button_about.set_tooltip_text("Control whether Hardware Clock is in Local Time or not")
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 8, 1, 1)

        label = Gtk.Label(label="9. Read time from HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 9, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_ABOUT)
        self.button_about.set_tooltip_text("Read the time from the Hardware Clock")
        self.button_about.connect("clicked", self.read_time_from_hw_clock)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 9, 1, 1)

        label = Gtk.Label(label="10. Synchronize HW Clock")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 10, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize Hardware Clock to System Time")
        self.button_about.connect("clicked", self.on_sync_hw_clock_to_system_time)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 10, 1, 1)

        label = Gtk.Label(label="11. Synchronize Time 2")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 11, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_about.set_tooltip_text("Synchronize System Time from Hardware Clock")
        self.button_about.connect("clicked", self.on_sync_system_time_from_hw_clock)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 11, 1, 1)

        label = Gtk.Label(label="12. Set Time manually")
        label.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
        grid.attach(label, Gtk.PositionType.LEFT, 12, 1, 1)
        self.button_about = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_about.set_tooltip_text("Set System Time manually")
        self.button_about.connect("clicked", self.on_set_time_manually)
        grid.attach(self.button_about, Gtk.PositionType.RIGHT, 12, 1, 1)

if __name__ == '__main__':
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()