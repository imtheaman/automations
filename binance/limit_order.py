import testConfig
import config
from binance.client import Client

# client = Client(testConfig.API_KEY, testConfig.SECRET_KEY, testnet=true)
client = Client(config.API_KEY, config.SECRET_KEY)
busd_pairs = ['BTCBUSD', 'ETHBUSD', 'BNBBUSD', 'ADABUSD', 'XRPBUSD', 'DOGEBUSD', 'SOLBUSD', 'FTTBUSD']
symbol = busd_pairs[0]
quantity = 2600
buyqty = sellqty = 0

def LiveTickerPrice():
    ticker = client.futures_orderbook_ticker(symbol=symbol)
    bidPrice = float(ticker['bidPrice'])
    askPrice = float(ticker['askPrice'])
    bidqty = float(ticker['bidQty'])
    askqty = float(ticker['askQty'])
    return [bidPrice, askPrice, bidqty, askqty]
def order_limit(order_type, sym,side,qty, price, reduce=False):
	if reduce == False:
		position = 'LONG' if side == 'BUY' else 'SHORT'
	else:
		position = 'SHORT' if side == 'BUY' else 'LONG'
	details = client.futures_create_order(symbol=sym,side=side,type=order_type, timeInForce='GTX', positionSide=position, postOnly=True,quantity=qty,price=price)
	return details

if __name__ == '__main__':
    
    print(order_limit('LIMIT', symbol, 'BUY', quantity, LiveTickerPrice()[0]))
    # # buyqty += float(limit_buy_quantity)
    # # print(buyqty, symbol,  "NOW IN ", limit_buy_pair, limit_buy_orderid, ' BUY')
    # # limit_buy_pair, limit_buy_orderid, limit_buy_quantity = 

    print(order_limit('LIMIT', symbol, 'SELL', quantity, LiveTickerPrice()[1]))
    # limit_sell_pair, limit_sell_orderid, limit_sell_quantity = 
    # sellqty += float(limit_sell_quantity)
    # print(sellqty, symbol,  "NOW IN ", limit_sell_pair, limit_sell_orderid, ' SELL')
