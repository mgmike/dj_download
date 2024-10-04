#!/bin/bash

input="spotify_playlists.txt"
download_path="/mnt/c/Users/mgmik/Documents/spotdl/"
final_path="/mnt/e/Music/spotDL/"

while IFS='|' read -r name url; do

    echo
    echo "*******************************"
    echo -e "Downloading $name, with url $url"
    echo "*******************************"
    
    spotdl download $url
    mv -n "$download_path$name/"* "$final_path$name"
    
done < "$input"
