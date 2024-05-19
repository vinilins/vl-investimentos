from enum import StrEnum

from beartype import beartype
from dataclasses import dataclass
from libs.basic_types.textual import Textual


class AssetType(StrEnum):
    STOCK = "STOCK"
    CRYPTO = "CRYPTO"


@dataclass
class Asset:
    name: Textual
    type: AssetType


@beartype
@dataclass
class AssetsRepository:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AssetsRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __post_init__(self):
        self.all_assets = list(
            map(lambda stock: Asset(name=Textual(stock), type=AssetType.STOCK), STOCKS)
        )

    def get_asset(self, name: str, asset_type: AssetType):
        result = list(
            filter(
                lambda asset: asset.name == name and asset.type == asset_type,
                self.all_assets,
            )
        )
        return result[0] if len(result) == 1 else None


STOCKS: set[str] = {"BBAS3", "KBLN11"}
