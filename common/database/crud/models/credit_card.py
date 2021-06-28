from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreditCardBase(BaseModel):
    AccountID: int


class CreditCardCreate(CreditCardBase):
    CreditCardNo: str
    EffectiveDate: str
    BankID: int
    CreditSeq: str
    CoBrandType: int
    CardType: int
    AliasName: Optional[str]
    Seq: int
    CardBrand: str
    CreateTime: datetime
    UpdateTime: datetime
    BindingOrderNo: Optional[str] = ""
    BindingStatus: int


class CreditCardUpdate(CreditCardBase):
    pass
