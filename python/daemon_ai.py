from file_util import FileUtil
from database import AudioDatabase
from ai_whisper import AiWhisper
from audio_converter import Converter
from time_util import TimeUtil
from log_util import LogUtil
import time
import sys

delay = 5

def main():
    LogUtil.writeln(f"Starting transcode...")
    model_index = 0

    if len(sys.argv) > 1:
        model_index = int(sys.argv[1])

    database = AudioDatabase()
    ai = AiWhisper(model_index)
    converter = Converter()
    iteration = 0
    while True:
        flow = ""
        iteration += 1
        log_key = f"AI Processing Iteration {iteration}"
        TimeUtil.start(log_key)
        try:
            data = database.get_from_queue_for_processing()
            if data:
                result = ai.transcode(file_path=data.audio_path)
                mp3 = converter.convert_to_mp3(path=data.audio_path)
                database.create_record(audio_path=mp3, speech=result)
                FileUtil.delete_file(data.audio_path)
                
                text_path = FileUtil.create_text_file_path()
                FileUtil.write_text_to_file(text_path, result)

                database.remove_from_queue(data.id)
                remaining_line_size = database.get_queue_size()
                LogUtil.writeln(f"Job done. Remeaing queue size: {remaining_line_size}")
            else:
                flow = "empty database"
                LogUtil.writeln(f"Empty database. Sleeping...")
                time.sleep(delay)
        except Exception as error:
            flow = "error"
            LogUtil.writeln(f"Error during a transcoding ${error}")
            time.sleep(delay)
        TimeUtil.end(log_key, flow)

if __name__ == "__main__":
    main()