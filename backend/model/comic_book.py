from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

import base


class Comic_Book(base):
    __tablename__ = 'comic_books'

    id = Column("pk_comic_book", Integer, primary_key=True)
    name = Column(String(120), unique=True)
    value = Column(Float)
    state = Column(String(15))
    insertion_date = Column(DateTime, default=datetime.now())


    def __init__(self, name:str, value:float, state:str,
                 insertion_date:Union[DateTime, None] = None):

        self.name = name
        self.value = value
        self.state = state
        self.insertion_date = insertion_date