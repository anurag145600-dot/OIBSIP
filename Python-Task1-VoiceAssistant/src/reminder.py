from dataclasses import dataclass
from datetime import datetime


@dataclass
class Reminder:

    message: str
    delay: int

    created_at: datetime = datetime.now()