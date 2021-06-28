from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    Phone: Optional[str]


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    PayBalance: Optional[Decimal]
    DepositBalance: Optional[Decimal]
    ReceiptBalance: Optional[Decimal]
    AdvanceBalance: Optional[Decimal]
    EscrowBalance: Optional[Decimal]
    JKOSCoin: Optional[int]
    UserLevel: Optional[int]
