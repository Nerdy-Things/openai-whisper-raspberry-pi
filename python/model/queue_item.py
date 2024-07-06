from dataclasses import dataclass
from datetime import datetime

@dataclass
class QueueItem:
    id: int
    audio_path: str
    in_process: int
    created: datetime
