from typing import Optional

from pydantic import BaseModel


class PurchaseMainBase(BaseModel):
    AccountID: Optional[str]
    JKOSID: Optional[str]


class PurchaseMainCreate(PurchaseMainBase):
    pass


class PurchaseMainUpdate(PurchaseMainBase):
    pass
