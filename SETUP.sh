#!/bin/bash

echo Installing Git...
sudo apt-get install git-all -yqq

echo Repository cloning...
cd /usr/local/bin
sudo git clone https://github.com/GraveFruit/SoundSphere.git

echo Installing SoundSphere...
cd SoundSphere
sudo sh INSTALL.sh
