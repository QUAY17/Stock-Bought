#requires robin_stocks

import robin_stocks
import robin_stocks.robinhood as r
import matplotlib.pyplot as plt
from time import sleep

def login(email, password):
	'''login to robinhood account'''
	r.login(email, password)


def get_quote(ticker):
	'''get quote (misc info) for a given company'''
	print(robin_stocks.robinhood.stocks.get_quotes(ticker))


def plot_hourly_historical(ticker):
	'''plot historical hourly price for the last day'''
	data = robin_stocks.robinhood.stocks.get_stock_historicals(ticker, interval='hour', span='day')
	prices = []
	times = []
	for datum in data:
		prices.append(float(datum['close_price']))
		times.append(datum['begins_at']) # needs better formatting

	plt.plot(range(len(prices)), prices)
	# may need to save the figure instead?
	plt.show()


def get_spot_price(ticker):
	'''get current price of a stock'''
	return r.get_latest_price(ticker)


