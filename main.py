import os
import random

from src.grabpayclient.requests import InitChargeRequest
from src.grabpayclient.common import *
from src.grabpayclient.client import GrabClient

from dotenv import load_dotenv

load_dotenv()


credentials = Credentials(
    partner_id=os.getenv("GRAB_PARTNER_ID"),
    partner_secret=os.getenv("GRAB_PARTNER_SECRET"),
    client_id=os.getenv("GRAB_CLIENT_ID"),
    client_secret=os.getenv("GRAB_CLIENT_SECRET"),
    merchant_id=os.getenv("GRAB_MERCHANT_ID"),
    redirect_url=os.getenv("GRAB_REDIRECT_URI"),
)

client = GrabClient(credentials=credentials)


def generate_random_string(length):
    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(possible) for _ in range(length))


random_string = f"{generate_random_string(5)}123"

req = InitChargeRequest(
    partner_group_tx_id=random_string,
    partner_tx_id=random_string,
    currency='SGD',
    amount=100,
    description='testing',
    merchant_id=credentials.merchant_id
)


response = client.init_charge(req)
print(response)
