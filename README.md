# Audio transcription with OpenAI Whisper on Raspberry PI 5

## Video Description
[![Watch the video](/thumbnail_1280_720.jpg)](https://www.youtube.com/watch?v=pH07mng2jBU)

## System folder

The system folder has the script `install.sh` that will install all required software for the test.

## Python folder

### The script daemon_audio

```python
python daemon_audio.py
```

will start a audio recording into a `/data` folder. The audio stream will be split on 10-second chunks and added to a queue for transcription.

### The script daemon_ai

```python
python daemon_ai.py 0
```

will start a audio transcription processing. It will grab audio files from `daemon_audio` (if any) and transcibe them into a `/data` folder. The transcript will be in a data folder in a `*_transcription.txt` files.

You can change OpenAI whispes models https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages :

```python
python daemon_audio.py 0 # tiny.en
python daemon_audio.py 1 # base.en	
python daemon_audio.py 2 # small.en	
python daemon_audio.py 3 # medium.en
```
