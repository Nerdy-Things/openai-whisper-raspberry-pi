import whisper
from time_util import TimeUtil

class AiWhisper:

    _models = ["tiny.en", "base.en", "small.en", "medium.en"]

    _model = None
    
    def __init__(self):
        TimeUtil.start("AiWhisper init")
        self._model = whisper.load_model(self._models[0])
        TimeUtil.end("AiWhisper init")

    def transcode(self, file_path: str):
        TimeUtil.start("AiWhisper transcode")
        result =self._model.transcribe(file_path, fp16=False, language='English')
        TimeUtil.end("AiWhisper transcode")
        return result["text"]
