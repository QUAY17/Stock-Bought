"""
* CSE326 Stock Bought 
* file: main.py
* authors: Jennifer Minnich
* date: Spring 2022
* Toolkit to extend the Robinhood Investment API
"""

import backtrader as bt
import yfinance as yf
from datetime import datetime
import matplotlib as plt
import pandas as pd

"""
* creates Donchian Strategy
* used to buy breakouts
* buy when the price breaks through the 20-period high and
* sell when the price drops below the 20-period low
"""

class DonchianStrategy(bt.Strategy):
    def __init__(self):
        self.myind = Donchian()

    def next(self):
        if self.data[0] > self.myind.dch[0]:
            self.buy()
        elif self.data[0] < self.myind.dcl[0]:
            self.sell()

class Donchian(bt.Indicator):
    '''
    Params Note:
      - `lookback` (default: -1)
        If `-1`, the bars to consider will start 1 bar in the past and the
        current high/low may break through the channel.
        If `0`, the current prices will be considered for the Donchian
        Channel. This means that the price will **NEVER** break through the
        upper/lower channel bands.
    '''

    alias = ('DCH', 'DonchianChannel',)

    lines = ('dcm', 'dch', 'dcl',)  # dc middle, dc high, dc low
    params = dict(
        period=20,
        lookback=-1,  # consider current bar or not
    )

    plotinfo = dict(subplot=False)  # plot along with data
    plotlines = dict(
        dcm=dict(ls='--'),  # dashed line
        dch=dict(_samecolor=True),  # use same color as prev line (dcm)
        dcl=dict(_samecolor=True),  # use same color as prev line (dch)
    )

    def __init__(self):
        hi, lo = self.data.high, self.data.low
        if self.p.lookback:  # move backwards as needed
            hi, lo = hi(self.p.lookback), lo(self.p.lookback)

        self.l.dch = bt.ind.Highest(hi, period=self.p.period)
        self.l.dcl = bt.ind.Lowest(lo, period=self.p.period)
        self.l.dcm = (self.l.dch + self.l.dcl) / 2.0  # avg of the above


"""
* creates 200 day Simple Moving Average (SMA) Strategy
* determines the long term general market trend
"""
class SMA200Strategy(bt.Strategy):

    def __init__(self):  # Initiation
        self.sma = bt.ind.SimpleMovingAverage()  # Processing

"""
* creates Average True Range (ATR) Strategy
* give an estimate of fluctuation in a given period
* iterates through the last 14 data points 
* takes the high and subtract the low for each period then averages it out
"""
class AverageTrueRange(bt.Strategy):

	def log(self, txt, dt=None):
		dt = dt or self.datas[0].datetime.date(0)
		print(f'{dt.isoformat()} {txt}') #Print date and close
		
	def __init__(self):
		self.dataclose = self.datas[0].close
		self.datahigh = self.datas[0].high
		self.datalow = self.datas[0].low
		
	def next(self):
		range_total = 0
		for i in range(-13, 1):
			true_range = self.datahigh[i] - self.datalow[i]
			range_total += true_range
		ATR = range_total / 14

		self.log(f'Close: {self.dataclose[0]:.2f}, ATR: {ATR:.4f}')

"""
* creates 50 day Simple Moving Average (SMA) Strategy
* determines the short term general market trend
* use the start and end date wrapper
"""
class SMA50Strategy(bt.SignalStrategy):
    def __init__(self):  # Initiation
        self.sma = bt.ind.SimpleMovingAverage(period=50)  # Processing
    
    def next(self):  # Processing
        if self.sma > self.data.close:
            self.buy()
        elif self.sma < self.data.close: # Post-processing
            self.close()

"""
* creates Dual Moving Average (DMA) Strategy
* SIGNAL_LONG is trading logic
"""        
class DMAStrategy(bt.SignalStrategy):
    def __init__(self):
        short, long = bt.ind.SMA(period=50), bt.ind.SMA(period=200)
        crossover = bt.ind.CrossOver(short, long)
        self.signal_add(bt.SIGNAL_LONG, crossover) #this is the trading logic

"""
* backtest function
* uses strategy selection from user
* ticker input from user
* cash input by user
* commission set to 0
"""
def backtest(strategy, ticker, fromdate, todate, cash, commission=0.00):

    # initialize the engine with your strategy, cash amount, etc
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy)
    cerebro.broker.setcash(cash)
    cerebro.broker.setcommission(commission=commission)

    # pulling the data to put into the engine
    data = bt.feeds.PandasData(dataname=yf.download(ticker, fromdate, todate))
    cerebro.adddata(data)

    # show portfolio stats before and after runnign the backtest
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # plot it
    plt.rcParams['figure.figsize'] = [15, 12]
    plt.rcParams.update({'font.size': 12}) 
    cerebro.plot(iplot=False)


if __name__ == '__main__':

    # backtest
    backtest(strategy=DMAStrategy, ticker='TSLA', fromdate='2018-01-01', todate='2022-04-01', cash=1000.0)
