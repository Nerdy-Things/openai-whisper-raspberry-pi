from dataclasses import dataclass
from datetime import datetime

@dataclass
class AudioItem:
    id: int
    audio_path: str
    speech: int
    created: datetime
