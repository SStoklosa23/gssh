import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BasicApp(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="GSSH Wrapper")
        self.set_default_size(400, 300)

        self.dark_mode = False

        user_label = Gtk.Label(label="User:")
        address_label = Gtk.Label(label="Address:")
        port_label = Gtk.Label(label="Port:")

        self.user_entry = Gtk.Entry()
        self.address_entry = Gtk.Entry()
        self.port_entry = Gtk.Entry()

        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.save_values)

        label_grid = Gtk.Grid()
        label_grid.attach(user_label, 0, 0, 1, 1)
        label_grid.attach(self.user_entry, 1, 0, 1, 1)
        label_grid.attach(address_label, 0, 1, 1, 1)
        label_grid.attach(self.address_entry, 1, 1, 1, 1)
        label_grid.attach(port_label, 0, 2, 1, 1)
        label_grid.attach(self.port_entry, 1, 2, 1, 1)

        for label in [user_label, address_label, port_label]:
            label.set_halign(Gtk.Align.CENTER)
            label.set_valign(Gtk.Align.CENTER)

        submit_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        submit_button_box.pack_start(submit_button, False, False, 0)

        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        center_box.pack_start(label_grid, False, False, 0)
        center_box.pack_start(submit_button_box, False, False, 0)

        main_alignment = Gtk.Alignment(xalign=0.5, yalign=0.5, xscale=0.5, yscale=0.5)
        main_alignment.add(center_box)

        self.add(main_alignment)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def save_values(self, widget):
        user = self.user_entry.get_text()
        address = self.address_entry.get_text()
        port = self.port_entry.get_text()
        print("User:", user)
        print("Address:", address)
        print("Port:", port)

    def toggle_mode(self, widget, state):
        self.dark_mode = state
        if self.dark_mode:
            Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", True)
        else:
            Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", False)

if __name__ == "__main__":
    app = BasicApp()
    Gtk.main()
