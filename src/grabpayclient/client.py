import json
from collections import namedtuple
from enum import Enum

import requests
import base64
import hashlib
import hmac

from typing import Tuple, TypeVar, Union, Type
from datetime import datetime
from http import HTTPStatus

from src.grabpayclient.requests import InitChargeRequest
from src.grabpayclient.helper import snake_to_camel

__all__ = ['GrabClient']

from src.grabpayclient.responses import InitChargeResponse

T = TypeVar('T')


class GrabClient:
    def __init__(self, credentials: Tuple[str, str], sandbox_mode=False):
        self.credentials = credentials
        self.sandbox_mode = sandbox_mode


    @property
    def base_url(self):
        """
        :return:
        """

        staging_url = "https://partner-api.stg-myteksi.com"
        production_url = "https://partner-api.grab.com"

        return staging_url if self.sandbox_mode else production_url

    def _http_post_json(self, url_path: str, payload: Union[dict, namedtuple], response_class: Type[T]) -> T:
        """

        :param url_path:
        :param payload:
        :param response_class:
        :return:
        """

        headers = self._headers()
        headers['Content-Type'] = 'application/json'
        data = self._serialize_request(payload)

        try:
            url = f"{self.base_url}{url_path}"
            http_response = requests.post(url, headers=headers, data=data, timeout=5)
            if http_response.status_code != HTTPStatus.OK:
                pass

            return response_class.from_api_json(http_response.json())
        except requests.RequestException as error:
            raise
        except ValueError as error:
            raise

    @staticmethod
    def _headers():
        return {
            "Date": datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
        }

    def _serialize_request(self, payload) -> str:
        """

        :param payload:
        :return:
        """
        return json.dumps(self._marshal_request(payload))

    @staticmethod
    def _marshal_request(payload) -> dict:
        """

        :param payload:
        :return:
        """
        marshalled = {}
        if isinstance(payload, dict):
            fields = payload.keys()
        else:
            if len(getattr(payload, '__slots__')) > 0:
                fields = getattr(payload, '__slots__')
            else:
                fields = getattr(payload, '_fields')

        for attr_name in fields:
            attr_val = getattr(payload, attr_name)
            camel_attr_name = snake_to_camel(attr_name)

            if isinstance(attr_val, datetime):
                marshalled[camel_attr_name] = int(attr_val.timestamp())
            elif isinstance(attr_val, Enum):
                marshalled[camel_attr_name] = attr_val.value
            elif isinstance(attr_val, (int, str, bool, float)):
                marshalled[camel_attr_name] = attr_val
            elif isinstance(attr_val, list):
                marshalled[camel_attr_name] = [GrabClient._marshal_request(element) for element in attr_val]
            else:
                marshalled[camel_attr_name] = GrabClient._marshal_request(attr_val)

        return marshalled

    def init_charge(self, req: InitChargeRequest) -> InitChargeResponse:
        """POST /grabpay/partner/v2/charge/init"""
        return self._http_post_json('/grabpay/partner/v2/charge/init', req, InitChargeResponse)
