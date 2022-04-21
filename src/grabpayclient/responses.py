from abc import ABCMeta, abstractmethod
from typing import NamedTuple, List


from src.grabpayclient.common import ChargeInitParam


class AbstractDeserializableResponse(metaclass=ABCMeta):
    __slots__ = ()

    @classmethod
    @abstractmethod
    def from_api_json(cls, api_json: dict):
        pass


class InitChargeResponse(AbstractDeserializableResponse):
    # {
    #   "partnerTxID": "5f1344c8dd6942858a05546bfe7e672f",
    #   request": "eyJhbGciOiAibm9uZSJ9.eyJjbGFpbXMiOnsidHJhbnNhY3Rpb24iOnsidHhJRCI6IjNiOGM2MmZiNmY0YzQyMjRiZDBlNzU0NDg4NzQ2Y2I4In19fQ."
    # }
    __slots__ = ('partner_tx_id', 'request')

    def __init__(self, partner_tx_id: str, request: str):
        self.partner_tx_id = partner_tx_id
        self.request = request

    @classmethod
    def from_api_json(cls, api_json: dict):
        return cls(
            partner_tx_id=api_json.get('partnerTxID'),
            request=api_json.get('request')
        )