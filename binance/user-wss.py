from binance.client import Client
import websocket
import config

client = Client(config.API_KEY, config.SECRET_KEY)
listenKey = client.futures_stream_get_listen_key()
ORDER_TRADE_UPDATE = ''
ACCOUNT_UPDATE = ''
MARGIN_CALL = ''

def on_message(message):
    global user_websocket_message
    user_websocket_message = message
    print(message)

ws = websocket.WebSocketApp(f"wss://fstream.binance.com/ws/{listenKey}", on_message=on_message)

if __name__=="__main__":
    ws.run_forever()
