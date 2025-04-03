from datetime import datetime

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    ISBN: str
    published: datetime
