import limit_order as l;

quantity = 1000
if __name__ == '__main__':
    print(l.order_limit('LIMIT', l.symbol, 'SELL', quantity, l.LiveTickerPrice()[1]))