# Clockwidget

Binds a hotkey to a huge digital clock widget that's rendered (hopefully) on top of your other applications.

## Dependencies and installing them
PyGObject, GTK and their dependencies
[Here's how!](https://pygobject.readthedocs.io/en/latest/etting_started.html#windows-getting-started)

You will also need [Pynput](https://pypi.org/project/pynput/)
```
pip3 install pynput
```

## One shot run / Trying it out
```
python3 main.py
```
Now press Ctrl+Shift+a, which is the default hotkey.
You should now be obtrusively greeted by the clock widget.

![https://github.com/steina1989/clockwidget/blob/master/demo.png]


## Modifying the hotkey
The hotket is relatively simple to modify to your liking, check out the self.key_combinations list in ClockListener (main.py) and the pynput documentation.

## Installing
Todo

## Known caveats
### Gnome
You may want to enable the [noAnnoyance plugin](https://extensions.gnome.org/extension/1236/noannoyance/) if the Clock widget opens in the background and you are greeted with Gnome's "Application Ready" message (it's a mad annoying feature anyway)
