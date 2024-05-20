from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src.message_bus.commands import Command
from src.wallet.domain.value_objects.assets import AssetType


@dataclass
class RegisterInvestiment(Command):
    asset_name: str
    asset_type: AssetType
    purchase_date: datetime
    quantity: int
    unit_price: Decimal
    other_costs: Decimal
