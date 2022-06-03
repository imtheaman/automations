import websocket

def onMessage(wssApp, msg):
    print(msg['b'])

wssApp = websocket.WebSocketApp('wss://stream.binance.com:9443/ws/btcbusd@depth', on_message=onMessage)
wssApp.run_forever()