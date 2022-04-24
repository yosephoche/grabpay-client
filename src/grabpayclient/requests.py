from typing import List, Optional
from src.grabpayclient.common import CurrencyCode


class WebUrlRequest:
    __slots__ = (
        "client_id", "scope", "response_type", "redirect_uri",
        "nonce", "state", "code_challenge_method", "code_challenge", "request", "acr_values"
    )

    def __init__(self, client_id, scope, response_type, redirect_uri, nonce, state,
                 code_challenge_method, code_challenge, request, acr_values):
        self.client_id = client_id
        self.scope = scope
        self.response_type = response_type,
        self.redirect_uri = redirect_uri,
        self.nonce = nonce,
        self.state = state,
        self.code_challenge_method = code_challenge_method,
        self.code_challenge = code_challenge,
        self.request = request,
        self.acr_values = acr_values

    @property
    def __dict__(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}


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
