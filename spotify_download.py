import subprocess
import os

format = 'mp3'

cwd = os.curdir
print(cwd)

# Make errors dir
if not os.path.exists('errors'):
    os.mkdir('errors') 

spotify_playlists = open('spotify_playlists.txt')
for playlist in spotify_playlists:
    playlist_name = playlist.split('|')[0]
    playlist_url = playlist.split('|')[1]
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
    subprocess.run(['spotdl', '--save-errors', f'../errors/{playlist_name} errors.txt', '--overwrite', 'skip', '--format', format, playlist_url], cwd=playlist_name)

spotify_playlists.close()