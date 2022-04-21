from time import sleep
import queue
import robin_stocks
import robin_stocks.robinhood as r

class sma50hr():

    def __init__(self, ticker):

        # initialize
        self.ticker = ticker
        self.kill_signal = False

        # Get data to create the moving average
        data = robin_stocks.robinhood.stocks.get_stock_historicals(self.ticker, interval='hour', span='week')
        prices = []
        for datum in data:
            prices.append(float(datum['close_price']))
            
        # Define a queue 50 points long for the moving average and fill it with the latest data
        self.baseline = queue.Queue(50)
        for price in prices[-50:]:
            self.baseline.put(price)


    def start_trading(self):

        # Live trade until the kill signal is sent
        while self.kill_signal is False:

            # calculate the moving average, can't do this directly on queue's so I dump it to a list to calculate
            self.moving_average = round(sum(list(self.baseline.queue)) / len(list(self.baseline.queue)), 2)
            print('Moving average', self.moving_average)

            # get the current spot price
            price = round(float(r.get_latest_price(self.ticker)[0]))
            print('Current price:', price)

            # trading logic:
            if price <= self.moving_average:
                print("Bought $1 of %s" % self.ticker)
                #rorder_buy_fractional_by_price(ticker, amountInDollars=1)

            else:
                print("Sold $1 of %s" % self.ticker)
                #r.order_sell_fractional_by_price(ticker, amountInDollars=1)

            # update the moving average with the recent datapoint and recompute the moving average
            # first remove the first point put in initially to make room using .get()
            self.baseline.get()
            self.baseline.put(price)

            # wait a few seconds before pulling prices again
            sleep(10)


    def return_details(self):
        return self.moving_average 