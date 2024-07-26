import whisper
from time_util import TimeUtil

class AiWhisper:

    _models = ["tiny.en", "base.en", "small.en", "medium.en"]

    _model = None

    def __init__(self, model_index: int = 0):
        TimeUtil.start("AiWhisper init")
        if len(self._models) < model_index:
            raise KeyError(f"Max model index is {len(self._models)}")
        print(f"AiWhisper init. Using {self._models[model_index]}")
        self._model = whisper.load_model(self._models[model_index])
        TimeUtil.end("AiWhisper init")

    def transcode(self, file_path: str):
        TimeUtil.start("AiWhisper transcode")
        result =self._model.transcribe(file_path, fp16=False, language='English')
        TimeUtil.end("AiWhisper transcode")
        return result["text"]
