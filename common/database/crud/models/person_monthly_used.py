from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class PersonMonthlyUsedBase(BaseModel):
    AccountID: Optional[int]


class PersonMonthlyUsedCreate(PersonMonthlyUsedBase):
    pass


class PersonMonthlyUsedUpdate(PersonMonthlyUsedBase):
    Month: int
    PaySubTotal: Optional[Decimal]
    PaySubTotalDailyOdd: Optional[Decimal]
    PaySubTotalDailyEven: Optional[Decimal]
    TransoutSubTotal: Optional[Decimal]
    TransoutSubTotalDailyOdd: Optional[Decimal]
    TransoutSubTotalDailyEven: Optional[Decimal]
    TransinSubTotal: Optional[Decimal]
    ReceiptSubTotal: Optional[Decimal]
    UpdateTime: Optional[datetime]
