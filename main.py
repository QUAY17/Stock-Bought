"""

CSE326 Stock Bought 
file: main.py
authors: Jennifer Minnich
date: Spring 2022
Toolkit to extend the Robinhood Investment API

"""
import backtrader as bt
import yfinance as yf
from datetime import datetime

"""
* acceses yahoo finance api
* ticker data  
* fundamentals 
* historical market data
"""
def ticker_data():

    msft = yf.Ticker("MSFT") #select ticker
    print(msft.info) # get fundamental data
    print(msft.history(period="max")) # get historical market data

"""
* creates trading strategy1
* Dual Moving Average (DMA) Strategy
"""

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=20)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

if __name__ == '__main__':

    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaCross)
    cerebro.broker.setcash(10337.0)
    cerebro.broker.setcommission(commission=0.001)

    # for testing purposes
    # stock needs to be user input var
    data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2017-01-01', '2017-12-31')) #robinhood

    cerebro.adddata(data)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()
