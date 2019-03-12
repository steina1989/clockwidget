#!/usr/bin/env bash
set -e

if [ -f /etc/systemd/system/clockwidget.service ]; then
    sudo systemctl disable clockwidget.service
fi

if [ -d /usr/local/bin/clockwidget ]; then
    sudo rm -rf /usr/local/bin/clockwidget 
fi

sudo mkdir /usr/local/bin/clockwidget
sudo cp main.py clock_widget.py styles.css /usr/local/bin/clockwidget

sudo chown -R $USER:$USER /usr/local/bin/clockwidget

echo \
"[Unit]
Description=ClockWidget
After=syslog.target

[Service]
User=$USER
WorkingDirectory=/usr/local/bin/clockwidget
ExecStart=/usr/local/bin/clockwidget/main.py
StandardOutput=syslog
StandardError=syslog
Environment=DISPLAY=:0
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
" | sudo tee /etc/systemd/system/clockwidget.service

sudo systemctl daemon-reload
sudo systemctl enable clockwidget.service
sudo systemctl start clockwidget.service