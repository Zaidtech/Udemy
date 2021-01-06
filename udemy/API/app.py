import requests

APP_ID =  "f26c7fcefed34b8a91c1d057a8ba0fe9"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

responce = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = responce.json()['rates']  # responce.json will give a dictionary and we are accessing a key ['rates']

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["GBP"]


print(f"Usd {usd_amount} is GBP {gbp_amount}")

