from pydantic import BaseModel
from typing import Optional

class Position(BaseModel):
    key: Optional[str] = ""
    cusip: Optional[str] = ""
    account: Optional[str] = ""
    netposition: Optional[float] = 0.0
    price: Optional[float] = 0.0
