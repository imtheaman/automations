import limit_order as l

if __name__ == '__main__':
    print(l.order_limit('LIMIT', "BTCBUSD", 'BUY', 0.002, l.LiveTickerPrice()[0], True))
# print(buyqty, reduce_buy_pair, 'REDUCE ONLY BUY',  reduce_buy_orderid)
# buyqty = 0
# reduce_buy_pair, reduce_buy_orderid = 

    print(l.order_limit('LIMIT', "BTCBUSD", 'SELL', 0.002, l.LiveTickerPrice()[1], True))
# print(sellqty, reduce_sell_pair, 'REDUCE ONLY SELL', reduce_sell_orderid)
# sellqty = 0
# reduce_sell_pair, reduce_sell_orderid = 