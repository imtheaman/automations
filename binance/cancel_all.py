from binance.client import Client
import config

client = Client(config.API_KEY, config.SECRET_KEY)
print(client.futures_cancel_all_open_orders())