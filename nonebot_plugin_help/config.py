from pydantic import BaseModel, Extra
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    # Your Config Here
    help_block: Optional[bool] = False
    help_priority: Optional[int] = 1
