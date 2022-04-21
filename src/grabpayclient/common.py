from enum import Enum
from typing import NamedTuple


__all__ = ["CurrencyCode", "ChargeInitParam", "Credentials"]


class Credentials(NamedTuple):
    partner_id: str
    partner_secret: str
    client_id: str
    client_secret: str
    merchant_id: str
    redirect_url: str


class CurrencyCode(Enum):
    sgd = "SGD"


class ChargeInitParam(NamedTuple):
    amount: int
    currency: CurrencyCode
    description: str
    merchantID: str
    partnerGroupTxID: str
    partnerTxID: str

