import limit_order as l;

quantity = 1600
if __name__ == '__main__':
    print(l.order_limit('LIMIT', l.symbol, 'BUY', quantity, l.LiveTickerPrice()[0]))