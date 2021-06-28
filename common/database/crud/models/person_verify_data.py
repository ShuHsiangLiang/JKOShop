from typing import Optional

from pydantic import BaseModel


class PersonVerifyDataBase(BaseModel):
    ID: Optional[int]


class PersonVerifyDataCreate(PersonVerifyDataBase):
    pass


class PersonVerifyDataUpdate(PersonVerifyDataBase):
    ResidentFront: Optional[str]
    ResidentBack: Optional[str]
