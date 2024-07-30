#!/bin/bash

sudo apt update
sudo apt-get install -y ffmpeg sqlite3  portaudio19-dev python3-pyaudio

# https://github.com/openai/whisper
pip install numpy==1.26.4 --break-system-packages
pip install -U openai-whisper --break-system-packages
pip install pyaudio --break-system-packages
pip install pydub --break-system-packages


# chmod +x ./create_daemon_files.sh
# sudo ./create_daemon_files.sh

