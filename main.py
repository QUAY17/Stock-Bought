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
import matplotlib as plt

"""
* creates trading strategy1
* Dual Moving Average (DMA) Strategy
"""

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=20)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

def backtest(strategy, ticker, fromdate, todate, cash=1000, commission=0.00):

    # initialize the engine with your strategy, cash amount, etc
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy)
    cerebro.broker.setcash(cash)
    cerebro.broker.setcommission(commission=commission)

    # pulling the data to put into the engine
    data = bt.feeds.PandasData(dataname=yf.download(ticker, fromdate, todate))
    cerebro.adddata(data)

    # run the backtest!
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # plot it, the extra plt commands for getting it inline, default doesn't work in colab
    plt.rcParams['figure.figsize'] = [15, 12]
    plt.rcParams.update({'font.size': 12}) 
    cerebro.plot(iplot=False)


if __name__ == '__main__':

    # backtest
    # call robinhood api 
    backtest(strategy=SmaCross, ticker='TSLA', fromdate='2017-01-01', todate='2020-12-31')
