from audio_recorder import AudioRecord
from file_util import FileUtil
from database import AudioDatabase
from time_util import TimeUtil
from log_util import LogUtil
import time

delay = 5

def main():
    LogUtil.writeln(f"Creating audio recorder...")
    recorder = AudioRecord()
    database = AudioDatabase()
    iteration = 0
    while True:
        flow = ""
        iteration += 1
        log_key = f"AI Processing Iteration {iteration}"
        TimeUtil.start(log_key)
        try:
            audio_file = FileUtil.create_audio_file_path()  
            TimeUtil.start(f"Recording {iteration}")
            recorded = recorder.record(audio_file)
            TimeUtil.end(f"Recording {iteration}")
            if (recorded):
                TimeUtil.start(f"Adding to db {iteration}")
                database.add_to_queue(audio_path=audio_file)
                TimeUtil.end(f"Adding to db {iteration}")
            else:
                flow = "failed"
                time.sleep(delay)
        except Exception as error:
            flow = "error"
            LogUtil.writeln(f"Error during a recording ${error}. Sleeping.")
            time.sleep(delay)
        TimeUtil.end(log_key, flow)

if __name__ == "__main__":
    main()