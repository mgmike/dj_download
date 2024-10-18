#!/bin/bash

input="spotify_playlists.txt"
download_path="/mnt/c/Users/mgmik/Documents/spotdl/"
final_path="/mnt/e/Music/deemix/"

while IFS='|' read -r name url; do

    echo
    echo "*******************************"
    echo -e "Downloading $name, with url $url"
    echo "*******************************"
    
    spotdl --archive "/mnt/c/Users/mgmik/Documents/spotdl/$name/archive.txt" download $url
    # mv -n "$download_path$name/"* "$final_path$name"
    python3 copy_new.py "$download_path$name" "$final_path$name"
    
done < "$input"
