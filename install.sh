# /usr/bin/bash
if [ -e /etc/systemd/system/fan_controller.service  ]; then
    sudo rm -rf /etc/systemd/system/fan_controller.service
fi
if [ -e /opt/fan_controller.py ]; then
    sudo rm -rf /opt/fan_controller.py
fi

sudo cp ./fan_controller.py /opt/fan_controller.py
sudo cp ./fan_controller.service /etc/systemd/system/fan_controller.service

sudo chmod 0755 /opt/fan_controller.py
sudo systemctl enable fan_controller.service
