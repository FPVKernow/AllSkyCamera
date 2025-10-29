#!/bin/bash
chmod u+x getDependencies.sh

echo "Getting dependencies for AllSkyCamera"

sudo apt-get install git
sudo apt-get install python3-pip
sudo apt-get install python-picamera
sudo apt-get install python3-picamera
##These will not work for non-pi systems