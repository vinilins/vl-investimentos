from datetime import datetime
from decimal import Decimal
from typing import Optional

from beartype import beartype
from pydantic import PositiveInt
from dataclasses import dataclass
from src.wallet.domain.value_objects.assets import Asset


@beartype
@dataclass
class Investment:
    asset: Asset
    purchase_date: datetime
    quantity: PositiveInt
    unit_price: Decimal
    other_costs: Decimal = Decimal("0.0")
    sale_date: Optional[datetime] = None

    @property
    def total_price(self) -> Decimal:
        return Decimal(self.unit_price * self.quantity + self.other_costs)
