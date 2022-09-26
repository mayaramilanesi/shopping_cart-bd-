import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field

from src.schemas.address import Address
from src.schemas.user import UserSchema


class OrderSchema(BaseModel):
    user: UserSchema
    create: datetime.datetime = Field(default=datetime.datetime.now())
    address: str
    authority: Optional[str] = Field(max_length=100)
