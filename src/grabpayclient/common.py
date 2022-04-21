from enum import Enum
from typing import NamedTuple


__all__ = ["CurrencyCode", "ChargeInitParam"]


class CurrencyCode(Enum):
    sgd = "SGD"


class ChargeInitParam(NamedTuple):
    amount: int
    currency: CurrencyCode
    description: str
    merchantID: str
    partnerGroupTxID: str
    partnerTxID: str

