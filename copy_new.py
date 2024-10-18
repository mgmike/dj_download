import os
import shutil
import sys

def parse_song_name(song_name):
    # Split the song name by '|', '(', and ')' and remove empty elements
    parts = [part.strip() for part in song_name.replace(' - ', '|').replace('.mp3', '').replace('(', '|').replace(')', '|').split('|') if part]
    # print(parts)
    return parts

def song_exists_in_destination(song_name, destination_songs):
    # Parse the source song and check for overlap with any destination song
    source_parts = set(parse_song_name(song_name))
    for dest_song in destination_songs:
        dest_parts = set(parse_song_name(dest_song))
        # print('Checking intersection between: ', source_parts, ' and ', dest_parts)
        counter = 0
        for part in dest_parts:
            if part != '':
                # print('Compare ', part, ' and ', source_parts)
                for part_s in source_parts:
                    if part in part_s:  # Check if there's any intersection
                        print('******** Confirmed! found ', part, ' in ', source_parts, '\n')
                        counter = counter + 1
        if counter >= len(dest_parts):
            return True
    return False

def main(source_dir, destination_dir):
    # Get list of files in both directories
    source_songs = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    destination_songs = [f.lower() for f in os.listdir(destination_dir) if os.path.isfile(os.path.join(destination_dir, f))]

    skipped = []
    copied = []

    for song in source_songs:
        if('archive.txt' in song):
            continue
        # Check if song should not be copied due to part overlap
        if song_exists_in_destination(song.lower(), destination_songs):
            print(f"*******Skipping {song}: Found matching part in destination folder.")
            skipped.append(song)
        else:
            # Copy the song to the destination folder
            shutil.move(os.path.join(source_dir, song), destination_dir)
            print(f"********Copied {song} to {destination_dir}")
            copied.append(song)

    print('\nSkipped songs: ')
    for skip in skipped:
        print(skip)
    print('\nCopied songs: ')
    for copy in copied:
        print(copy) 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    # Check if both directories exist
    if not os.path.isdir(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        sys.exit(1)
    
    if not os.path.isdir(destination_directory):
        print(f"Destination directory '{destination_directory}' does not exist. Making new")
        # Make errors dir
        os.mkdir(destination_directory) 

    # Run the main function
    main(source_directory, destination_directory)