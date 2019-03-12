# Clockwidget

Binds a hotkey to a huge digital clock widget that's rendered (hopefully) on top of your other applications.

## Dependencies and installing them
Python3

PyGObject, GTK and their dependencies
[Here's how!](https://pygobject.readthedocs.io/en/latest/getting_started.html#windows-getting-started)

You will also need [Pynput](https://pypi.org/project/pynput/)
```
pip3 install pynput
```

## One shot run / Trying it out
```
python3 main.py
```
Now press Ctrl+alt+t, which is the default hotkey.
You should now be obtrusively greeted by the clock widget.

![](https://github.com/steina1989/clockwidget/blob/master/demo.png)


## Modifying the hotkey
The hotkey is relatively simple to modify to your liking, check out the self.key_combinations list in ClockListener (main.py) and the pynput documentation.

## Installing (WIP)
### OS with systemd (Debian, Arch, etc.)
```
chmod +x install.sh
./install.sh
```
If something is wrong, try debugging with
```
sudo journalctl -f -u clockwidget.service
```


## Known caveats
### Gnome
You may want to enable the [noAnnoyance plugin](https://extensions.gnome.org/extension/1236/noannoyance/) if the Clock widget opens in the background and you are greeted with Gnome's "Application Ready" message (it's a mad annoying feature anyway)

There seems to be some disrepancies between operating systems, especially regarding how successfully the application of css is (clock is rendered with small font size)

It has however been verified to work on Ubuntu 18.10 with Vanilla Gnome installed.

## This has been a March installment of 2019's A-Program-A-Month