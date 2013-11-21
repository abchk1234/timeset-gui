#!/usr/bin/python2
import shlex
import subprocess
from gi.repository import Gtk

program_icon = "/usr/share/icons/Faenza/apps/48/time-admin.png"

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
        sp = subprocess.Popen(shlex.split('hwclock -D'), stdout=subprocess.PIPE)
        out2, err = sp.communicate()
        textbuffer.set_text("{0}\n{1}".format(out, out2))
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
        textbuffer.set_text("{0}".format(out))

        window2.connect("destroy", lambda q: Gtk.main_quit())
        window2.show_all()
        Gtk.main()

class sync_system_time_from_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Sync system time from H/W clock", parent,
            Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Synchronize system time from hardware clock.\nClick OK and wait a few moments while the time is being synchronised\n')
        box.add(label)
        self.show_all()

class control_the_hw_clock(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Control the HW clock", parent,
            Gtk.DialogFlags.MODAL, buttons=("UTC", Gtk.ResponseType.OK, "Local Time", Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Set the hardware clock to use - \n')
        box.add(label)
        self.show_all()

class set_ntp_at_statup(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Enable or disable NTP", parent,
            Gtk.DialogFlags.MODAL, buttons=("Enable", Gtk.ResponseType.OK, "Disable", Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enable or disable NTP usage.\nNTP stands for Network Time Protocol.\nIf NTP is enabled the computer will periodically\nsynchronize time from the internet.')
        box.add(label)
        self.show_all()

class set_timezone(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set timezone", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            "List timezones", Gtk.ResponseType.APPLY,
            Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        label = Gtk.Label('Enter the timezone. It should be like \nContinent/City - Europe/Berlin')
        box.add(label)
        listz = Gtk.ListStore(str)
        for timezone in [
"Africa/Abidjan",
"Africa/Accra",
"Africa/Addis_Ababa",
"Africa/Algiers",
"Africa/Asmara",
"Africa/Bamako",
"Africa/Bangui",
"Africa/Banjul",
"Africa/Bissau",
"Africa/Blantyre",
"Africa/Brazzaville",
"Africa/Bujumbura",
"Africa/Cairo",
"Africa/Casablanca",
"Africa/Ceuta",
"Africa/Conakry",
"Africa/Dakar",
"Africa/Dar_es_Salaam",
"Africa/Djibouti",
"Africa/Douala",
"Africa/El_Aaiun",
"Africa/Freetown",
"Africa/Gaborone",
"Africa/Harare",
"Africa/Johannesburg",
"Africa/Juba",
"Africa/Kampala",
"Africa/Khartoum",
"Africa/Kigali",
"Africa/Kinshasa",
"Africa/Lagos",
"Africa/Libreville",
"Africa/Lome",
"Africa/Luanda",
"Africa/Lubumbashi",
"Africa/Lusaka",
"Africa/Malabo",
"Africa/Maputo",
"Africa/Maseru",
"Africa/Mbabane",
"Africa/Mogadishu",
"Africa/Monrovia",
"Africa/Nairobi",
"Africa/Ndjamena",
"Africa/Niamey",
"Africa/Nouakchott",
"Africa/Ouagadougou",
"Africa/Porto-Novo",
"Africa/Sao_Tome",
"Africa/Tripoli",
"Africa/Tunis",
"Africa/Windhoek",
"America/Adak",
"America/Anchorage",
"America/Anguilla",
"America/Antigua",
"America/Araguaina",
"America/Argentina/Buenos_Aires",
"America/Argentina/Catamarca",
"America/Argentina/Cordoba",
"America/Argentina/Jujuy",
"America/Argentina/La_Rioja",
"America/Argentina/Mendoza",
"America/Argentina/Rio_Gallegos",
"America/Argentina/Salta",
"America/Argentina/San_Juan",
"America/Argentina/San_Luis",
"America/Argentina/Tucuman",
"America/Argentina/Ushuaia",
"America/Aruba",
"America/Asuncion",
"America/Atikokan",
"America/Bahia",
"America/Bahia_Banderas",
"America/Barbados",
"America/Belem",
"America/Belize",
"America/Blanc-Sablon",
"America/Boa_Vista",
"America/Bogota",
"America/Boise",
"America/Cambridge_Bay",
"America/Campo_Grande",
"America/Cancun",
"America/Caracas",
"America/Cayenne",
"America/Cayman",
"America/Chicago",
"America/Chihuahua",
"America/Costa_Rica",
"America/Creston",
"America/Cuiaba",
"America/Curacao",
"America/Danmarkshavn",
"America/Dawson",
"America/Dawson_Creek",
"America/Denver",
"America/Detroit",
"America/Dominica",
"America/Edmonton",
"America/Eirunepe",
"America/El_Salvador",
"America/Fortaleza",
"America/Glace_Bay",
"America/Godthab",
"America/Goose_Bay",
"America/Grand_Turk",
"America/Grenada",
"America/Guadeloupe",
"America/Guatemala",
"America/Guayaquil",
"America/Guyana",
"America/Halifax",
"America/Havana",
"America/Hermosillo",
"America/Indiana/Indianapolis",
"America/Indiana/Knox",
"America/Indiana/Marengo",
"America/Indiana/Petersburg",
"America/Indiana/Tell_City",
"America/Indiana/Vevay",
"America/Indiana/Vincennes",
"America/Indiana/Winamac",
"America/Inuvik",
"America/Iqaluit",
"America/Jamaica",
"America/Juneau",
"America/Kentucky/Louisville",
"America/Kentucky/Monticello",
"America/Kralendijk",
"America/La_Paz",
"America/Lima",
"America/Los_Angeles",
"America/Lower_Princes",
"America/Maceio",
"America/Managua",
"America/Manaus",
"America/Marigot",
"America/Martinique",
"America/Matamoros",
"America/Mazatlan",
"America/Menominee",
"America/Merida",
"America/Metlakatla",
"America/Mexico_City",
"America/Miquelon",
"America/Moncton",
"America/Monterrey",
"America/Montevideo",
"America/Montserrat",
"America/Nassau",
"America/New_York",
"America/Nipigon",
"America/Nome",
"America/Noronha",
"America/North_Dakota/Beulah",
"America/North_Dakota/Center",
"America/North_Dakota/New_Salem",
"America/Ojinaga",
"America/Panama",
"America/Pangnirtung",
"America/Paramaribo",
"America/Phoenix",
"America/Port-au-Prince",
"America/Port_of_Spain",
"America/Porto_Velho",
"America/Puerto_Rico",
"America/Rainy_River",
"America/Rankin_Inlet",
"America/Recife",
"America/Regina",
"America/Resolute",
"America/Rio_Branco",
"America/Santa_Isabel",
"America/Santarem",
"America/Santiago",
"America/Santo_Domingo",
"America/Sao_Paulo",
"America/Scoresbysund",
"America/Sitka",
"America/St_Barthelemy",
"America/St_Johns",
"America/St_Kitts",
"America/St_Lucia",
"America/St_Thomas",
"America/St_Vincent",
"America/Swift_Current",
"America/Tegucigalpa",
"America/Thule",
"America/Thunder_Bay",
"America/Tijuana",
"America/Toronto",
"America/Tortola",
"America/Vancouver",
"America/Whitehorse",
"America/Winnipeg",
"America/Yakutat",
"America/Yellowknife",
"Antarctica/Casey",
"Antarctica/Davis",
"Antarctica/DumontDUrville",
"Antarctica/Macquarie",
"Antarctica/Mawson",
"Antarctica/McMurdo",
"Antarctica/Palmer",
"Antarctica/Rothera",
"Antarctica/Syowa",
"Antarctica/Vostok",
"Arctic/Longyearbyen",
"Asia/Aden",
"Asia/Almaty",
"Asia/Amman",
"Asia/Anadyr",
"Asia/Aqtau",
"Asia/Aqtobe",
"Asia/Ashgabat",
"Asia/Baghdad",
"Asia/Bahrain",
"Asia/Baku",
"Asia/Bangkok",
"Asia/Beirut",
"Asia/Bishkek",
"Asia/Brunei",
"Asia/Choibalsan",
"Asia/Chongqing",
"Asia/Colombo",
"Asia/Damascus",
"Asia/Dhaka",
"Asia/Dili",
"Asia/Dubai",
"Asia/Dushanbe",
"Asia/Gaza",
"Asia/Harbin",
"Asia/Hebron",
"Asia/Ho_Chi_Minh",
"Asia/Hong_Kong",
"Asia/Hovd",
"Asia/Irkutsk",
"Asia/Jakarta",
"Asia/Jayapura",
"Asia/Jerusalem",
"Asia/Kabul",
"Asia/Kamchatka",
"Asia/Karachi",
"Asia/Kashgar",
"Asia/Kathmandu",
"Asia/Khandyga",
"Asia/Kolkata",
"Asia/Krasnoyarsk",
"Asia/Kuala_Lumpur",
"Asia/Kuching",
"Asia/Kuwait",
"Asia/Macau",
"Asia/Magadan",
"Asia/Makassar",
"Asia/Manila",
"Asia/Muscat",
"Asia/Nicosia",
"Asia/Novokuznetsk",
"Asia/Novosibirsk",
"Asia/Omsk",
"Asia/Oral",
"Asia/Phnom_Penh",
"Asia/Pontianak",
"Asia/Pyongyang",
"Asia/Qatar",
"Asia/Qyzylorda",
"Asia/Rangoon",
"Asia/Riyadh",
"Asia/Sakhalin",
"Asia/Samarkand",
"Asia/Seoul",
"Asia/Shanghai",
"Asia/Singapore",
"Asia/Taipei",
"Asia/Tashkent",
"Asia/Tbilisi",
"Asia/Tehran",
"Asia/Thimphu",
"Asia/Tokyo",
"Asia/Ulaanbaatar",
"Asia/Urumqi",
"Asia/Ust-Nera",
"Asia/Vientiane",
"Asia/Vladivostok",
"Asia/Yakutsk",
"Asia/Yekaterinburg",
"Asia/Yerevan",
"Atlantic/Azores",
"Atlantic/Bermuda",
"Atlantic/Canary",
"Atlantic/Cape_Verde",
"Atlantic/Faroe",
"Atlantic/Madeira",
"Atlantic/Reykjavik",
"Atlantic/South_Georgia",
"Atlantic/St_Helena",
"Atlantic/Stanley",
"Australia/Adelaide",
"Australia/Brisbane",
"Australia/Broken_Hill",
"Australia/Currie",
"Australia/Darwin",
"Australia/Eucla",
"Australia/Hobart",
"Australia/Lindeman",
"Australia/Lord_Howe",
"Australia/Melbourne",
"Australia/Perth",
"Australia/Sydney",
"Europe/Amsterdam",
"Europe/Andorra",
"Europe/Athens",
"Europe/Belgrade",
"Europe/Berlin",
"Europe/Bratislava",
"Europe/Brussels",
"Europe/Bucharest",
"Europe/Budapest",
"Europe/Busingen",
"Europe/Chisinau",
"Europe/Copenhagen",
"Europe/Dublin",
"Europe/Gibraltar",
"Europe/Guernsey",
"Europe/Helsinki",
"Europe/Isle_of_Man",
"Europe/Istanbul",
"Europe/Jersey",
"Europe/Kaliningrad",
"Europe/Kiev",
"Europe/Lisbon",
"Europe/Ljubljana",
"Europe/London",
"Europe/Luxembourg",
"Europe/Madrid",
"Europe/Malta",
"Europe/Mariehamn",
"Europe/Minsk",
"Europe/Monaco",
"Europe/Moscow",
"Europe/Oslo",
"Europe/Paris",
"Europe/Podgorica",
"Europe/Prague",
"Europe/Riga",
"Europe/Rome",
"Europe/Samara",
"Europe/San_Marino",
"Europe/Sarajevo",
"Europe/Simferopol",
"Europe/Skopje",
"Europe/Sofia",
"Europe/Stockholm",
"Europe/Tallinn",
"Europe/Tirane",
"Europe/Uzhgorod",
"Europe/Vaduz",
"Europe/Vatican",
"Europe/Vienna",
"Europe/Vilnius",
"Europe/Volgograd",
"Europe/Warsaw",
"Europe/Zagreb",
"Europe/Zaporozhye",
"Europe/Zurich",
"Indian/Antananarivo",
"Indian/Chagos",
"Indian/Christmas",
"Indian/Cocos",
"Indian/Comoro",
"Indian/Kerguelen",
"Indian/Mahe",
"Indian/Maldives",
"Indian/Mauritius",
"Indian/Mayotte",
"Indian/Reunion",
"Pacific/Apia",
"Pacific/Auckland",
"Pacific/Chatham",
"Pacific/Chuuk",
"Pacific/Easter",
"Pacific/Efate",
"Pacific/Enderbury",
"Pacific/Fakaofo",
"Pacific/Fiji",
"Pacific/Funafuti",
"Pacific/Galapagos",
"Pacific/Gambier",
"Pacific/Guadalcanal",
"Pacific/Guam",
"Pacific/Honolulu",
"Pacific/Johnston",
"Pacific/Kiritimati",
"Pacific/Kosrae",
"Pacific/Kwajalein",
"Pacific/Majuro",
"Pacific/Marquesas",
"Pacific/Midway",
"Pacific/Nauru",
"Pacific/Niue",
"Pacific/Norfolk",
"Pacific/Noumea",
"Pacific/Pago_Pago",
"Pacific/Palau",
"Pacific/Pitcairn",
"Pacific/Pohnpei",
"Pacific/Port_Moresby",
"Pacific/Rarotonga",
"Pacific/Saipan",
"Pacific/Tahiti",
"Pacific/Tarawa",
"Pacific/Tongatapu",
"Pacific/Wake",
"Pacific/Wallis"]:
            listz.append([timezone])
        completion = Gtk.EntryCompletion()
        completion.set_model(listz)
        completion.set_text_column(0)
        self.entry = Gtk.Entry()
        self.entry.set_completion(completion)
        box.add(self.entry)
        self.show_all()

class set_time_manually(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Set time", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_OK, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        box = self.get_content_area()
        label = Gtk.Label('Enter the time. The time may be formatted\nlike this: 2013-11-18 09:12:45\nor use just "hh:mm"')
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
            dialog2.format_secondary_text(
                "{0}".format(err))
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "System time synchronized to hardware clock!")
            dialog2.format_secondary_text(
                "{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def on_sync_hw_clock_to_system_time(self, widget):
        sp = subprocess.Popen(shlex.split("hwclock -w"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Warning !")
            dialog2.format_secondary_text(
                "{0}".format(err))
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Hardware clock synchronized to system time!")
            dialog2.format_secondary_text(
                "{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def on_control_the_hw_clock(self, widget):
        dialog = control_the_hw_clock(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Hardware Clock set to UTC !")
            dialog2.format_secondary_text(
                    "")
            dialog2.run()
            dialog2.destroy()
        if response == Gtk.ResponseType.CANCEL:
                sp = subprocess.Popen(shlex.split('timedatectl set-local-rtc 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = sp.communicate()
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Hardware Clock set to Local !")
                dialog2.format_secondary_text(
                    "")
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def on_set_ntp_at_statup(self, widget):
        dialog = set_ntp_at_statup(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-ntp 1'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "NTP enabled!")
            dialog2.format_secondary_text(
                    "")
            dialog.destroy()
            dialog2.run()
            dialog2.destroy()
        dialog.destroy()
        if response == Gtk.ResponseType.CANCEL:
            sp = subprocess.Popen(shlex.split('timedatectl set-ntp 0'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "NTP disabled !")
            dialog2.format_secondary_text(
                    "")
            dialog.destroy()
            dialog2.run()
            dialog2.destroy()
        dialog.destroy()

    def on_sync_from_network(self, widget):
        sp = subprocess.Popen(shlex.split("ntpdate -u 0.pool.ntp.org"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if err:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                Gtk.ButtonsType.OK, "Warning !")
            dialog2.format_secondary_text(
                "Cannot synchronize from the network right now.\nMake sure that you are running this program as root and try again.")
            dialog2.run()
            dialog2.destroy()
        else:
            dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Success ! Time updated.")
            dialog2.format_secondary_text("{0}".format(out))
            dialog2.run()
            dialog2.destroy()

    def show_timezones(self, widget):
        on_show_timezones()

    def show_current_date_and_time(self, widget):
        on_show_current_date_and_time()

    def on_set_timezones(self, widget):
        dialog = set_timezone(self)
        response = dialog.run()
        entered_text = dialog.entry.get_text()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-timezone "{0}"'.format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning!")
                dialog2.format_secondary_text(
                    "{0} is not a valid timezone".format(entered_text))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Timezone Changed!")
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        if response == Gtk.ResponseType.APPLY:
            dialog.destroy()
            on_show_timezones()
        dialog.destroy()

    def on_set_time_manually(self, widget):
        dialog = set_time_manually(self)
        response = dialog.run()
        entered_text = dialog.entry.get_text()
        if response == Gtk.ResponseType.OK:
            sp = subprocess.Popen(shlex.split('timedatectl set-time "{0}"'.format(entered_text)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sp.communicate()
            if err:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
                    Gtk.ButtonsType.OK, "Warning !")
                dialog2.format_secondary_text(
                    "{0} is not a valid time".format(entered_text))
                dialog2.run()
                dialog2.destroy()
            else:
                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Time Changed !")
                dialog2.format_secondary_text("{0}".format(out))
                dialog2.run()
                dialog2.destroy()
        dialog.destroy()

    def __init__(self):
        Gtk.Window.__init__(self, title="TimeSet - Manage System Date and Time")

        self.set_icon_from_file(program_icon)
        self.set_border_width(6)
        self.set_size_request(280, 300)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        self.add(vbox)

        grid = Gtk.Grid()
        grid.set_row_spacing(1)
        grid.set_column_spacing(1)
        vbox.add(grid)

        label = Gtk.Label(label="1. Show current date and time configuration")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 1, 1, 1)
        self.button_1 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_INFO)
        self.button_1.set_tooltip_text("Show Current Date and Time Configuration")
        self.button_1.connect("clicked", self.show_current_date_and_time)
        grid.attach(self.button_1, Gtk.PositionType.RIGHT, 1, 1, 1)

        label = Gtk.Label(label="2. Adjust the system timezone manually")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 3, 1, 1)
        self.button_2 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_2.set_tooltip_text("Set System Timezone")
        self.button_2.connect("clicked", self.on_set_timezones)
        grid.attach(self.button_2, Gtk.PositionType.RIGHT, 3, 1, 1)

        label = Gtk.Label(label="3. Synchronize the time from the network")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 4, 1, 1)
        self.button_3 = Gtk.ToolButton(stock_id=Gtk.STOCK_YES)
        self.button_3.set_tooltip_text("Synchronize the time from the network using NTP")
        self.button_3.connect("clicked", self.on_sync_from_network)
        grid.attach(self.button_3, Gtk.PositionType.RIGHT, 4, 1, 1)

        label = Gtk.Label(label="4. Choose whether NTP is enabled or not")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 5, 1, 1)
        self.button_4 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_4.set_tooltip_text("Control whether NTP is used for system time or not")
        self.button_4.connect("clicked", self.on_set_ntp_at_statup)
        grid.attach(self.button_4, Gtk.PositionType.RIGHT, 5, 1, 1)

        label = Gtk.Label(label="5. Hardware Clock in UTC or Local time")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 8, 1, 1)
        self.button_5 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_5.connect("clicked", self.on_control_the_hw_clock)
        self.button_5.set_tooltip_text("Control whether Hardware Clock is in Local Time or not")
        grid.attach(self.button_5, Gtk.PositionType.RIGHT, 8, 1, 1)

        label = Gtk.Label(label="6. Synchronize the H/W Clock to system time")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 10, 1, 1)
        self.button_6 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_6.set_tooltip_text("Synchronize Hardware Clock to System Time")
        self.button_6.connect("clicked", self.on_sync_hw_clock_to_system_time)
        grid.attach(self.button_6, Gtk.PositionType.RIGHT, 10, 1, 1)

        label = Gtk.Label(label="7. Synchronize system time to H/W clock")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 11, 1, 1)
        self.button_7 = Gtk.ToolButton(stock_id=Gtk.STOCK_APPLY)
        self.button_7.set_tooltip_text("Synchronize System Time from the Hardware Clock")
        self.button_7.connect("clicked", self.on_sync_system_time_from_hw_clock)
        grid.attach(self.button_7, Gtk.PositionType.RIGHT, 11, 1, 1)

        label = Gtk.Label(label="8. Adjust the system date and time manually")
        label.set_alignment(0, .5)
        grid.attach(label, Gtk.PositionType.LEFT, 12, 1, 1)
        self.button_8 = Gtk.ToolButton(stock_id=Gtk.STOCK_DIALOG_QUESTION)
        self.button_8.set_tooltip_text("Adjust the system date and time manually")
        self.button_8.connect("clicked", self.on_set_time_manually)
        grid.attach(self.button_8, Gtk.PositionType.RIGHT, 12, 1, 1)

if __name__ == '__main__':
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()