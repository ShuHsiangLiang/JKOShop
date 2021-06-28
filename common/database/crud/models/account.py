from typing import Optional

from pydantic import BaseModel


class AccountBase(BaseModel):
    ID: Optional[str]
    JKOSID: Optional[str]


class AccountCreate(AccountBase):
    pass


class AccountUpdate(AccountBase):
    ReleaseFunction: Optional[int]
    UpdateTime: Optional[str]
