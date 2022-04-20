import backtrader as bt
import yfinance as yf
from datetime import datetime
import matplotlib as plt

"""
creates Dual Moving Average (DMA) Strategy
* SIGNAL_LONG is trading logic
* by default, backtrader buys/sells one asset
"""

class DMAStrategy(bt.SignalStrategy):
    def __init__(self):
        short, long = bt.ind.SMA(period=50), bt.ind.SMA(period=200)
        crossover = bt.ind.CrossOver(short, long)
        self.signal_add(bt.SIGNAL_LONG, crossover) #this is the trading logic
  
"""
* creates 200 day Simple Moving Average (SMA) Strategy
* determines the long term general market trend
"""
class SMA200Strategy(bt.Strategy):

    def __init__(self):  # Initiation
        self.sma = bt.ind.SimpleMovingAverage(period=200)  # Processing

    def next(self):  # Processing
        if self.sma > self.data.close:
            self.buy()
        elif self.sma < self.data.close: # Post-processing
            self.close()


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

def saveplots(cerebro, numfigs=1, iplot=True, start=None, end=None,
            width=20, height=12, dpi=300, tight=True, use=None, file_path = '', **kwargs):

    from backtrader import plot
    if cerebro.p.oldsync:
        plotter = plot.Plot_OldSync(**kwargs)
    else:
        plotter = plot.Plot(**kwargs)

    figs = []
    for stratlist in cerebro.runstrats:
        for si, strat in enumerate(stratlist):
            rfig = plotter.plot(strat, figid=si * 100,
                                numfigs=numfigs, iplot=iplot,
                                start=start, end=end, use=use)
            figs.append(rfig)

    for fig in figs:
        for f in fig:
            f.savefig(file_path, bbox_inches='tight')
    return figs

"""
* backtest function
* uses strategy selection from user
* ticker input from user
* cash input by user
* commission set to 0
* adding the sizers will scale trades bt.sizers, possible add-on as features
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
    #cerebro.addsizer(bt.sizers.AllInSizer)
    
    # show portfolio stats before and after runnign the backtest
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

    saveplots(cerebro, file_path = 'savefig.png') #run it

    # plot it
    #plt.rcParams['figure.figsize'] = [15, 12]
    #plt.rcParams.update({'font.size': 12}) 
    #cerebro.plot()
    #saves plot as png 
    #figure = cerebro.plot(volume=False)[0][0]
    #figure.savefig('backtest_plot.png')


if __name__ == '__main__':

    # backtest
    # todate +1 day for most recent closing price
    backtest(strategy=SMA200Strategy, ticker='TSLA', fromdate='2018-01-01', todate='2022-04-21', cash=1000.0)