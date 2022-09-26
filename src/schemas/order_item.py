import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field

from src.schemas.order import OrderSchema
from src.schemas.product import ProductSchema


class OrderItemSchema(BaseModel):
    order: OrderSchema
    product: ProductSchema
    price: Decimal = Field(max_digits=10, decimal_places=2)
    paid: bool = Field(default=False)