from time import sleep
import queue
import robin_stocks

def kill_switch(bool):
    if bool is True:
        kill_signal = True
    else:
        kill_signal = False

    return kill_signal

def sma50hr(ticker, kill_signal):
    '''do some trading based around the 50-hour moving average'''

    # get data to create the moving average:
    data = robin_stocks.robinhood.stocks.get_stock_historicals(ticker, interval='hour', span='week')
    prices = []
    for datum in data:
        prices.append(float(datum['close_price']))
        
    # Define a queue 50 points long for the moving average and fill it with the latest data
    baseline = queue.Queue(50)
    for price in prices[-50:]:
        baseline.put(price)

    while kill_signal is False:

        # calculate the moving average, can't do this directly on queue's so I dump it to a list to calculate
        moving_average = round(sum(list(baseline.queue)) / len(list(baseline.queue)), 2)
        print('Moving average', moving_average)

        # get the current spot price
        price = round(float(r.get_latest_price(ticker)[0]))
        print('Current price:', price)

        # trading logic:
        if price <= moving_average:
            print("buy")
        else:
            print("sell")

        # update the moving average with the recent datapoint and recompute the moving average
        # first remove the first point put in initially to make room using .get()
        baseline.get()
        baseline.put(price)

        # wait a few seconds before pulling prices again
        sleep(10)