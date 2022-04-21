import re
import json
import hashlib
import base64
import hmac
import time

from urllib import parse


def snake_to_camel(text: str) -> str:
    return re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).upper(), text.replace('url', 'URL').replace('_id', '_ID'))


def compute_hmac(partner_secret, request_url, request_body, timestamp) -> str:
    request_path = parse.urlparse(request_url).path
    request_body = json.dumps(request_body).encode('utf-8')

    hash_payload = hashlib.new('sha256')
    hash_payload.update(request_body)
    hashed_payload = base64.b64encode(hash_payload.digest()).decode()
    raw = '\n'.join(["POST", "application/json", timestamp, request_path, hashed_payload])
    raw = [raw, '\n']
    raw = "".join(raw)

    signature = base64.b64encode(hmac.new(partner_secret.encode(), raw.encode(), hashlib.sha256).digest())
    return signature.decode()


def generate_pop_signature(access_token: str, client_secret: str) -> str:
    timestamp_unix = time.time().__round__()
    message = str(timestamp_unix) + access_token

    hmac_sign = hmac.new(client_secret.encode(), message.encode(), hashlib.sha256).digest()
    signature = base64.b64encode(hmac_sign)
    sub = signature.replace(b'=', b'').replace(b'+', b'-').replace(b'/', b'_').decode()
    payload = {
        "time_since_epoch": timestamp_unix,
        "sig": sub
    }

    payload_bytes = json.dumps(payload).encode()

    result = base64.b64encode(payload_bytes).decode().replace('=', '').replace('+', '-').replace('/', '_')

    return result
