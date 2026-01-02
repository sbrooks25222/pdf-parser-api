from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime

class ParseResponse(BaseModel):
    id: int
    filename: str
    doc_type: str
    extracted: Any
    created_at: datetime
