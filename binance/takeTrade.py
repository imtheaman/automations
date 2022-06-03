from binance.client import Client
from binance import BinanceSocketManager
import config
from datetime import datetime

client = Client(config.API_KEY, config.SECRET_KEY)
busd_pairs = ['BTCBUSD', 'ETHBUSD', 'BNBBUSD', 'ADABUSD', 'XRPBUSD', 'DOGEBUSD', 'SOLBUSD', 'FTTBUSD']
symbol = busd_pairs[0]

def LiveTickerPrice():
    ticker = client.futures_orderbook_ticker(symbol=symbol)
    bidPrice = float(ticker['bidPrice'])
    askPrice = float(ticker['askPrice'])
    bidqty = float(ticker['bidQty'])
    askqty = float(ticker['askQty'])
    return [bidPrice, askPrice, bidqty, askqty]
# ##### Place order function
def order_limit(order_type, sym,side,qty, price, reduce=False):
	if reduce == False:
		position = 'LONG' if side == 'BUY' else 'SHORT'
	else:
		position = 'SHORT' if side == 'BUY' else 'LONG'
	details = client.futures_create_order(symbol=sym,side=side,type=order_type, timeInForce='GTX', positionSide=position, postOnly=True,quantity=qty,price=price)
	return details

# ##### Place limit Buy + Sell order

# limit_buy_pair, limit_buy_orderid = order_limit('LIMIT', symbol, 'BUY', quantity, LiveTickerPrice()[0])
# buyqty += quantity
# print(buyqty, symbol,  "NOW IN ", limit_buy_pair, limit_buy_orderid, ' BUY')

limit_sell_pair, limit_sell_orderid = order_limit('LIMIT', symbol, 'SELL', quantity, LiveTickerPrice()[1])
sellqty += quantity
print(sellqty, symbol,  "NOW IN ", limit_sell_pair, limit_sell_orderid, ' SELL')

# ##### Place reduce only order

reduce_buy_pair, reduce_buy_orderid = order_limit('LIMIT', symbol, 'BUY', 0.020, LiveTickerPrice()[0], True)
print(buyqty, reduce_buy_pair, 'REDUCE ONLY BUY',  reduce_buy_orderid)
buyqty = 0

reduce_sell_pair, reduce_sell_orderid = order_limit('LIMIT', symbol, 'SELL', sellqty, LiveTickerPrice()[1], True)
print(sellqty, reduce_sell_pair, 'REDUCE ONLY SELL', reduce_sell_orderid)
sellqty = 0












































# bsm = BinanceSocketManager(client)

# # ##### Variables

# symbol = 'BTCBUSD'

# # ##### Server status

# status = client.get_system_status()
# print(f"Server is Working {status['msg']}".upper())

# # ##### Get all tickers

# # for ticker in client.futures_orderbook_ticker():
# #     print(ticker)
# #     print(ticker['symbol'].ljust(12), "   ", ticker['price'])

# # ##### Get Daily Balance Snapshot

# print('Time          ', '          Balance')
# for snap in client.get_account_snapshot(type='FUTURES')['snapshotVos']:
#     updateTime = datetime.fromtimestamp(snap['updateTime']/1000)
#     if len(snap['data']['assets']) > 1:
#         wallet2Balance = snap['data']['assets'][1]['walletBalance']
#     else: wallet2Balance = 0
#     walletBalance = float(snap['data']['assets'][0]['walletBalance']) + float(wallet2Balance)
#     print(updateTime, '   ',walletBalance)

# # ##### Get order book of a symbol

# # order_book = client.get_order_book(symbol=symbol)
# # print(f"Updated Time: {datetime.fromtimestamp(order_book['lastUpdateId']/1000)}")
# # bids = order_book['bids']
# # asks = order_book['asks']
# # print('Bids(buy orders)   Asks(sell orders) ')
# # for i in range(0, len(bids)):
# #     bidAmount = round(float(bids[i][0]),4)
# #     bidQuantity = round(float(bids[i][1]))
# #     askAmount = round(float(asks[i][0]),4)
# #     askQuantity = round(float(asks[i][1]))
# #     print(f"{str(bidAmount).ljust(5, '0')}  {str(bidQuantity).ljust(10)}   {str(askAmount).ljust(5, '0')}  {str(askQuantity).ljust(10)}")


# # ##### Income Stats

# income_history = client.futures_income_history()
# totalIncome = 0
# for income in income_history:
#     symbol = income['symbol']
#     incomeType = income['incomeType']
#     incomeAmount = round(float(income['income']),2)
#     time = datetime.fromtimestamp(income['time']/1000)
#     if incomeType != 'TRANSFER':
#         totalIncome += incomeAmount
#         print(f"{time} {symbol} {incomeType.ljust(25)} {str(incomeAmount).rjust(5)} {income['asset']}")
#     else: 
#         print('============================================================')
#         print(f"{time} {symbol} {incomeType.ljust(25)} {str(incomeAmount).rjust(5)} {income['asset']}")
#         print('============================================================')
# print('Total Income : ', totalIncome)

# # ##### Adding data to sqlite db

# # connection = sqlalchemy.create_engine(f'sqlite:///{symbol}klines1m.sqlite')

# # format for klines data
# def addtosqlite(klines):
#         df = pd.DataFrame(klines, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'total trades' , 'taker buy base asset vol', 'taker buy quote asset vol', 'ignore'], dtype=float)
#         df.to_sql(symbol, connection, if_exists='append', index=False)

# # ##### Historical Klines

# # socket
# # klines_data = client.futures_historical_klines(symbol,Client.KLINE_INTERVAL_1MINUTE, "10 Feb, 2022", "12 Feb, 2022")
# # # klineformatting(klines_data)
# # addtosqlite(klines_data)

# # ##### Live Tickers Socket

# ticker = client.futures_orderbook_ticker(symbol=symbol)
# bidPrice = float(ticker['bidPrice'])
# askPrice = float(ticker['askPrice'])
# print(bidPrice, askPrice)

# ##### Available BUSD and USDT pairs
# store_exchangeData = client.futures_exchange_info()['symbols']
# busd_futures_pairs = []
# usdt_futures_pairs = []
# for data in store_exchangeData:
#     if 'BUSD' in data['symbol'][-4:]:
#         busd_futures_pairs.append(data['pair'])
#     elif 'USDT' in data['symbol'][-4:]:
#         usdt_futures_pairs.append(data['pair'])
# print("BUSD Pairs: ", busd_futures_pairs)
# print('----------------------------------')
# print("USDT Pairs: ", usdt_futures_pairs)

# for pair in busd_futures_pairs:
#     client.futures_change_leverage(symbol=pair, leverage=5)
# while True:
#     await socket.__aenter__()
#     msg = await socket.recv()
#     print(msg)

# engine = sqlalchemy.create_engine(f'sqlite:///{symbol}stream.sqlite')

# # format for live trade data
# def createframe(msg):
#     df = pd.DataFrame([msg['data']])
#     df = df.loc[:, ['s', 'E', 'p']]
#     df.columns = ['symbol', 'Time', 'Price']
#     df.Price = df.Price.astype(float)
#     df.Time = pd.to_datetime(df.Time, unit='ms')
#     return df

# while True:
#     await socket.__aenter__()
#     msg = await socket.recv()
#     frame = createframe(msg)
#     frame.to_sql(symbol, engine, if_exists='append', index=False)





# %%
