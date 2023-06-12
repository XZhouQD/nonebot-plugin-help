from pydantic import BaseModel, Extra
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    # Your Config Here
    help_block: Optional[bool] = False
    help_priority: Optional[int] = 1
    ignore_plugins: Optional[list] = []
    to_me: Optional[bool] = False
