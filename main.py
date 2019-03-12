#!/usr/bin/env python3
from clock_widget import Clock
from pynput import keyboard


class ClockListener:
    def __init__(self):

        self.key_combinations = [
            {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char="a")},
            {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char="A")},
        ]

        self.pressed = set()

        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()

    def on_release(self, key):
        self.pressed.discard(key)

    def on_press(self, key):
        self.pressed.add(key)
        if self.check_for_combination():
            return False  # Stops the listener.
        return True

    def check_for_combination(self):
        for combination in self.key_combinations:
            if combination == self.pressed:
                return True
        return False


if __name__ == "__main__":
    while True:
        ClockListener()  # Blocks until key combination correct
        Clock()  # Blocks until any key depressed
