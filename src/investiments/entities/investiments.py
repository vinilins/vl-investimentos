from dataclasses import dataclass
from datetime import datetime

from src.investiments.value_objects.assets import Asset


@dataclass
class Investment:
    asset: Asset
    purchase_date: datetime
    sale_date: datetime
