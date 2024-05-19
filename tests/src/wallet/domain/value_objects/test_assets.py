import pytest
from beartype.roar import BeartypeCallHintParamViolation

from libs.basic_types.textual import Textual
from src.wallet.domain.value_objects.assets import Asset, AssetType


def test_create_asset():
    name = Textual("VALE3")

    vale3 = Asset(
        name=name,
        type=AssetType.STOCK,
    )

    assert vale3.name == "VALE3"
    assert vale3.type == "STOCK"


def test_create_asset_name_validation_error():
    name = "VALE3"

    with pytest.raises(BeartypeCallHintParamViolation):
        Asset(
            name=name,
            type=AssetType.STOCK,
        )


def test_create_asset_type_validation_error():
    name = Textual("VALE3")

    with pytest.raises(BeartypeCallHintParamViolation):
        Asset(
            name=name,
            type="STOCK",
        )
