#!/bin/bash
echo Adding autostart...
sudo mv -f /usr/local/bin/SoundSphere/soundsphere.desktop /etc/xdg/autostart

echo Updating repository list...
sudo apt-get update -yqq

echo Updating existing software...
sudo apt-get upgrade -yqq

echo Installing Chromium...
sudo apt-get install chromium-browser -yqq

echo Installing Python interpreter...
sudo apt-get install python2.7 -yqq

echo Installing additional software...
sudo apt-get install python-tk -yqq

for i in 10 9 8 7 6 5 4 3 2 1
do
        echo "Installation completed. System reboot in: $i"
        sleep 1
done
sudo shutdown -r now


