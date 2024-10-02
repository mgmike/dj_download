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

mkdir ~/yt-dlp/
cp yt-dlp.conf ~/yt-dlp/config