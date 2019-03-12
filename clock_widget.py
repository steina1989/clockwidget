#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import time


class Clock(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Overlay")

        # Ask OS not to render titlebar.
        Gtk.Window.set_decorated(self, False)

        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        self.apply_style()

        self.time_label = Gtk.Label(label=self.time_string())
        self.add(self.time_label)
    
        GLib.timeout_add(1000, self.update_time)

        self.connect("destroy", Gtk.main_quit)
        self.connect("key-release-event", self.kill)

        Gtk.Window.set_keep_above(self, True)
        self.show_all()
        Gtk.Window.maximize(self)

        Gtk.main()

    def update_time(self):
        self.time_label.set_text(self.time_string())
        # Needed to keep life going
        return "The answer to the great question is 42"

    def kill(self, widget, event):
        self.destroy()

    def apply_style(self):
        style_provider = Gtk.CssProvider()

        style_provider.load_from_path("styles.css")

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        # Transparent window
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        self.set_app_paintable(True)

    @staticmethod
    def time_string():
        return time.strftime("%H:%M:%S")
