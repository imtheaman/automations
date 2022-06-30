import talib, numpy

my_data = numpy.genfromtxt('historical_candlestick_5m.csv', delimiter=',') #np-array

close = my_data[:,4]
rsi = numpy.around(talib.RSI(close), 4)
print(rsi)
macd = talib.MACD(close)
print('==============================================')
for i in macd:
    print(numpy.around(i, 3))