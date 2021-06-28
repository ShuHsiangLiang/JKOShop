from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PersonExtendDataBase(BaseModel):
    AccountID: str


class PersonExtendDataCreate(PersonExtendDataBase):
    pass


class PersonExtendDataUpdate(PersonExtendDataBase):
    TransactionPwd: Optional[str]
    PwdErrorCount: Optional[int]
    UpdatePasswordAt: Optional[datetime]
    DeviceCode: Optional[str]
    UpdateDevicedAt: Optional[datetime]
