#!/bin/bash

input="youtube_playlists.txt"
yt_dlp_path="/mnt/e/Music/yt-dlp/"

while IFS='|' read -ra line; do
    playlist_name="${line[0]}"
    playlist_url="${line[1]}"

    echo
    echo "*******************************"
    echo -e "Downloading $playlist_name, with url $playlist_url"
    echo "*******************************"
    
    mkdir -p $yt_dlp_path
    yt-dlp --config-locations yt-dlp.conf "$playlist_url"

done <$input
