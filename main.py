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

class DonchianChannels(bt.Indicator):
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


class MyStrategy(bt.Strategy):
    def __init__(self):
        self.myind = DonchianChannels()

    def next(self):
        if self.data[0] > self.myind.dch[0]:
            self.buy()
        elif self.data[0] < self.myind.dcl[0]:
            self.sell()

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
    backtest(strategy=MyStrategy, ticker='TSLA', fromdate='2017-01-01', todate='2020-12-31')
