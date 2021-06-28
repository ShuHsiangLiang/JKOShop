from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MemberCardBase(BaseModel):
    AccountID: int


class MemberCardCreate(MemberCardBase):
    MemberCardID: str
    CardNo: Optional[str]
    IsDelete: int
    CardType: int
    CreateTime: datetime
    UpdateTime: datetime
    ExpireDate: datetime
    Balance: int


class MemberCardUpdate(MemberCardBase):
    pass
