#!/bin/bash

if [[ -z "$1" ]]
then
    echo "Enter a username for spotfy"
else
    spotdl --user-auth "$1" &
fi

pip install spotdl &
pip install --upgrade spotdl &
spotdl --download-ffmpeg
cp spotdl.json ~/.spotdl/config.json 

# python3 -m pip install -U --pre "yt-dlp[default]"
sudo add-apt-repository ppa:tomtomtom/yt-dlp &
sudo apt update &
sudo apt install yt-dlp 

mkdir ~/yt-dlp/
cp ./yt-dlp.conf ~/yt-dlp/config