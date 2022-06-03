# %init
import sqlalchemy
import pandas as pd
from binance.client import Client
import config
binance_client = Client(config.API_KEY, config.SECRET_KEY)

# %store -r symbol
symbol = 'BTCUSDT'
leverage = 1
balance_earlier = 0

# ##### Api status
status = binance_client.get_account_api_trading_status()
print(status)

# ##### Reading data from database
# engine = sqlalchemy.create_engine(f'sqlite:///{symbol}klines1m.sqlite')
# df = pd.read_sql(symbol, engine)
# df

# ##### Live account event socket

# ##### Check balance
# def checkFuturesBalance():
#     account = binance_client.futures_account()
#     return account['totalWalletBalance']

# print(checkFuturesBalance())

# ##### Check profit after last trade
# def profitInLastTrade():
#     global balance_earlier
#     balance_now = checkFuturesBalance()
#     return round((float(balance_now) - balance_earlier), 2)

# print(profitInLastTrade())

# ##### Change leverage
def changeLeverage(symbol,leverage):
    change = binance_client.futures_change_leverage(symbol=symbol, leverage=leverage)
    return change

print(changeLeverage(symbol,leverage))

# ##### Get First bid and ask

# while True:
#     print(LiveTickerPrice())


# ##### Get Orders
# print(binance_client.futures_get_open_orders())
# print('____________________')

# recent_trades = binance_client.futures_account_trades()
# print(recent_trades[::-1])



# ##### Get order details
# def getOrderDetails(symbol,id):
#     order = binance_client.futures_get_order(symbol=symbol, orderId=id)
#     print(order['status'])

# getOrderDetails(pair, order_id)

# ##### Cancel order

# def cancelOrder(symbol, id):
#     order = binance_client.futures_cancel_order(symbol=symbol, orderId=id)
#     for order in orders_list:
#         orders_list.pop()
#     print(order['status'])

# cancelOrder(limit_buy_pair, limit_buy_orderid)

# ##### Cancel all orders once
# print(binance_client.futures_cancel_all_open_orders())


d = binance_client.futures_exchange_info()
for i in d['symbols']:
    p = changeLeverage(i['symbol'], 1)
    print(p)