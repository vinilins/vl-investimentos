from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from src.wallet.domain.value_objects.assets import AssetType


class RequestRegisterInvestment(BaseModel):
    asset_name: str
    asset_type: AssetType
    purchase_date: datetime
    quantity: int
    unit_price: Decimal
    other_costs: Decimal


class ResponseRegisterInvestment(BaseModel):
    status: int = 200
    detail: str = "Successfully registered investment"
