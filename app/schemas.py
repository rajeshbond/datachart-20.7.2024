
from datetime import datetime , date
from operator import le
from pydantic import BaseModel, EmailStr , conint
from typing import Optional
from app.models import *
from pydantic.types import conlist




class DataFetch(BaseModel):
    conditionName: str

class DataFetchout(BaseModel):
    nsecode : str
    per_chg : float
    close: float
    date : str
    sector:str
    count : int
    frequency : int
    Piotrski : int
    

class frequencyFetchIn(BaseModel):
    tableName: str
    nsecode: str
    count: int
class frequencyFetchOut(BaseModel):
    nsecode : str
    close: float   
    date : str
    # time : str
    


   
    