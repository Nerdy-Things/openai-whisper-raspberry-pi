import pydub
from time_util import TimeUtil

class Converter:
    def convert_to_mp3(self, path: str):
        TimeUtil.start("MP3 Conertation")
        sound = pydub.AudioSegment.from_wav(path)
        result_path = path.replace(".wav", ".mp3")
        sound.export(result_path, format="mp3")
        TimeUtil.end("MP3 Conertation")
        return result_path
