import time
from log_util import LogUtil

class TimeUtil:
    
    _times = {}

    @staticmethod
    def start(key: str):
        TimeUtil._times[key] = time.time()

    @staticmethod
    def end(key: str, additionalInfo: str = ""):
        start_time = TimeUtil._times[key]
        try:
            del TimeUtil._times['key']
        except KeyError:
            pass
        end_time = time.time()
        execution_time = round((end_time - start_time) * 1000)
        text = f"{key}: TIME {execution_time} {additionalInfo}"
        LogUtil.writeln(text)
