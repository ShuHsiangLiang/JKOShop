from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BankAccountBase(BaseModel):
    AccountID: int


class BankAccountCreate(BankAccountBase):
    MsgNo: str
    Seq: int
    BankID: int
    Name: str
    AccountNo: str
    BankBranchID: Optional[int]
    BankBranchCode: Optional[str]
    OwnerName: str
    DisabledDraw: int
    CreateTime: datetime
    RealAccountNo: str
    IdentityAccount: str
    RealBankBranchID: int
    BankType: int
    Status: int
    IsDelete: int
    AccountStatus: Optional[int]
    AccountAuditDate: Optional[datetime]
    UpdateTime: datetime
    AccountRemitUnableRefundDate: Optional[datetime]
    AuditReason: Optional[str]


class BankAccountUpdate(BankAccountBase):
    IsDelete: int
    UpdateTime: datetime
