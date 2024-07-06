from datetime import datetime
import os
import os 

audio_folder = "audio"
data_folder = "data"
database_file = "database.db"
python_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.dirname(python_path) 

class FileUtil:
    @staticmethod
    def write_text_to_file(file_path: str, line: str) -> bool:
        with open(file_path, 'a') as the_file:
            the_file.write(f'{line} ')

    @staticmethod
    def create_text_file_path() -> str:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        directory = os.path.join(data_path, data_folder, year, month, day)
        file_name = f"{year}_{month}_{day}_transcription.txt"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, file_name)
        return file_path
    


    @staticmethod
    def create_log_file_path() -> str:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        directory = os.path.join(data_path, data_folder, year, month, day)
        file_name = f"{year}_{month}_{day}_log.txt"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, file_name)
        return file_path

    @staticmethod
    def create_audio_file_path() -> str:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        directory = os.path.join(data_path, data_folder, year, month, day, audio_folder)
        timestamp = now.strftime("%H_%M_%S_%f")[:-3]  # Format: HHMMSS_millis
        file_name = f"{timestamp}.wav"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, file_name)
        return file_path
    
    @staticmethod
    def delete_file(path: str) -> bool:
        if os.path.isfile(path=path):
            os.remove(path=path) 
            return True
        else:
            return False
        
    @staticmethod
    def get_database_path() -> str:
        directory = os.path.join(data_path , data_folder)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return os.path.join(directory, database_file)
        