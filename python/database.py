import sqlite3
import os
from typing import List, Type, TypeVar, Any
from datetime import datetime
from model.queue_item import QueueItem
from model.audio_item import AudioItem
from file_util import FileUtil

T = TypeVar('T')

database = sqlite3.connect(FileUtil.get_database_path())
database.row_factory = sqlite3.Row

audio_queue_db = "audio_queue"
audio_queue_create_statement = f"""
CREATE TABLE IF NOT EXISTS {audio_queue_db} 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    audio_path TEXT DEFAULT NULL,
    in_process INT DEFAULT 0,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

audio_record_db = "audio_record"
audio_record_create_statement = f"""
CREATE TABLE IF NOT EXISTS {audio_record_db} 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    audio_path TEXT DEFAULT NULL, 
    speech TEXT DEFAULT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

database.execute(audio_queue_create_statement)
database.execute(audio_record_create_statement)

class AudioDatabase: 

    def convert_rows(self, dataclass_type: Type[T], rows: List[sqlite3.Row]) -> List[T]:
        results = []
        for row in rows:
            row_dict = dict(row)
            if 'created' in row_dict:  # Convert the created field to datetime
                row_dict['created'] = datetime.strptime(row_dict['created'], "%Y-%m-%d %H:%M:%S")
            results.append(dataclass_type(**row_dict))
        return results

    def add_to_queue(self, audio_path: str) -> int:
        try:
            cursor=database.cursor()
            cursor.execute(f"""
                INSERT INTO {audio_queue_db} (audio_path) VALUES ('{audio_path}')
            """)
            database.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def get_from_queue_for_processing(self) -> dict:
        cursor=database.cursor()
        cursor.execute(f"""
            SELECT * FROM {audio_queue_db} WHERE in_process = 0 ORDER BY id ASC LIMIT 1 
        """)
        data = cursor.fetchall()
        if data:
            data = self.convert_rows(QueueItem, data)[0]
            database.execute(f"""
                UPDATE {audio_queue_db} set in_process = 1 where id = {data.id}
            """)
            database.commit()
        return data
    
    def create_record(self, audio_path: str, speech: str) -> int:
        cursor=database.cursor()
        insert_user_sql = f"""
            INSERT INTO {audio_record_db} (audio_path, speech) VALUES (?, ?)
        """
        cursor.execute(insert_user_sql, (audio_path, speech))
        database.commit()
        return cursor.lastrowid
    
    def print_records(self) -> int:
        cursor=database.cursor()
        cursor.execute(f"""
            SELECT * FROM {audio_record_db}
        """)
        data = cursor.fetchall()
        data = self.convert_rows(AudioItem, data)
        print(data)
        return data
    
    def remove_from_queue(self, id: int) -> bool:
        cursor=database.cursor()
        cursor.execute(f"""
            DELETE FROM {audio_queue_db} WHERE id = ?
        """, (str(id),))
        database.commit()
        return cursor.rowcount > 0
    
    def get_queue_size(self) -> int:
        cursor=database.cursor()
        cursor.execute(f"""SELECT count(1) as cnt FROM {audio_queue_db}""")
        database.commit()
        return cursor.fetchone()['cnt']
