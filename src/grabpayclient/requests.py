from typing import List, Optional
from src.grabpayclient.common import CurrencyCode


class InitChargeRequest:
    __slots__ = (
        'partner_group_tx_id', 'partner_tx_id', 'currency', 'amount', 'description', 'merchant_id', 'hide_payment_methods'
    )

    def __init__(self, partner_group_tx_id: str, partner_tx_id: str, currency: str, amount: int,
                 description: str, merchant_id: str, hide_payment_methods: Optional[List] = None):
        self.partner_group_tx_id = partner_group_tx_id
        self.partner_tx_id = partner_tx_id
        self.currency = currency
        self.amount = amount
        self.description = description
        self.merchant_id = merchant_id

        if not hide_payment_methods:
            self.hide_payment_methods = ["INSTALMENT"]

    @property
    def __dict__(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}
