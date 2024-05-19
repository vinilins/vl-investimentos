from datetime import datetime
from decimal import Decimal

from src.wallet.domain.entities.investments import Investment
from src.wallet.domain.value_objects.assets import AssetsRepository, AssetType


def test_create_investiments():
    asset_name = "BBAS3"

    asset = AssetsRepository().get_asset(name=asset_name, asset_type=AssetType.STOCK)

    bbas3 = Investment(
        asset=asset,
        purchase_date=datetime(2024, 1, 1),
        quantity=14,
        unit_price=Decimal("28.56"),
    )

    assert bbas3.asset.name == "BBAS3"
    assert bbas3.asset.type == AssetType.STOCK
    assert bbas3.purchase_date == datetime(2024, 1, 1)
    assert bbas3.quantity == 14
    assert bbas3.unit_price == Decimal("28.56")
    assert bbas3.total_price == Decimal("399.84")
