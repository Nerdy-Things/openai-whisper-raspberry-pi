#!/bin/bash

USER=$(whoami)
SERVICE_DIR="/etc/systemd/system"

# Copy files to services
sudo cp nerdy_things_ai_transcription.service $SERVICE_DIR/nerdy_things_ai_transcription.service
sudo cp nerdy_things_audio_recorder.service $SERVICE_DIR/nerdy_things_audio_recorder.service

sed "s/__USER__/$USER/g" nerdy_things_ai_transcription.service > "tmp.file"
sudo cp "tmp.file" "$SERVICE_DIR/nerdy_things_ai_transcription.service"
rm tmp.file

sed "s/__USER__/$USER/g" nerdy_things_audio_recorder.service > "tmp.file"
sudo cp "tmp.file" "$SERVICE_DIR/nerdy_things_audio_recorder.service"
rm tmp.file

# Reload systemd, enable and start the services
sudo systemctl daemon-reload

sudo systemctl enable nerdy_things_audio_recorder.service
sudo systemctl start nerdy_things_audio_recorder.service
sudo systemctl status nerdy_things_audio_recorder.service

sudo systemctl enable nerdy_things_ai_transcription.service
sudo systemctl start nerdy_things_ai_transcription.service
sudo systemctl status nerdy_things_ai_transcription.service