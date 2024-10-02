import subprocess
import os

format = 'mp3'

# Make errors dir
if not os.path.exists('errors'):
    os.mkdir('errors')
