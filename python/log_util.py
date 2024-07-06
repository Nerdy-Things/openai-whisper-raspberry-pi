from file_util import FileUtil

class LogUtil:

    @staticmethod
    def writeln(text: str):
        log_file = FileUtil.create_log_file_path()
        FileUtil.write_text_to_file(log_file, line=f"{text}\n")
        print(text)