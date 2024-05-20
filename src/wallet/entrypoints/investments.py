from fastapi import APIRouter

from src.wallet.domain.commands.investments import RegisterInvestiment
from src.wallet.entrypoints.schemas import (
    RequestRegisterInvestment,
    ResponseRegisterInvestment,
)

router = APIRouter()


@router.post(
    "/investments",
    summary="Register a new Investment in a Wallet",
    response_model=ResponseRegisterInvestment,
)
async def register_investment(
    order: RequestRegisterInvestment,
):
    result = RegisterInvestiment(
        asset_name=order.asset_name,
        asset_type=order.asset_type,
        purchase_date=order.purchase_date,
        quantity=order.quantity,
        unit_price=order.unit_price,
        other_costs=order.other_costs,
    )

    return result
