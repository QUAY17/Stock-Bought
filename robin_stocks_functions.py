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


"""
Order (Buy/Sell) Functions
Several functions below are redundant. I've put them in place in advance to be later culled depending on which of two styles of function call we decide to use.
"""

#Cancels all stock orders
def cancel_all_stock_orders():
	return r.orders.cancel_all_stock_orders()
	#Returns the list of orders that were cancelled.


#Cancels a specific order.
def cancel_stock_order(orderID):
	return r.orders.cancel_stock_order(orderID)
	#Returns the order information for the order that was cancelled.


#Returns a list of all the orders that are currently open.
def get_all_open_stock_orders():
	return r.orders.get_all_open_stock_orders(info = None)
	#Returns a list of dictionaries of key/value pairs for each order. If info parameter is provided, a list of strings is returned where the strings are the value of the key that matches info.


#Returns a list of all the orders that have been processed for the account.
def get_all_stock_orders():
	return r.orders.get_all_stock_orders(info = None)
	#Returns a list of dictionaries of key/value pairs for each order. If info parameter is provided, a list of strings is returned where the strings are the value of the key that matches info.


#Returns the information for a single order.
def get_stock_order_info(orderID):
	return r.orders.get_stock_order_info(orderID)
	#Returns a list of dictionaries of key/value pairs for the order.


#A generic order function.
def order(symbol, quantity, side):
	return r.orders.order(symbol, quantity, side, limitPrice = None, stopPrice = None, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#symbol (str) – The stock ticker of the stock to sell.
	#quantity (int) – The number of stocks to sell.
	#side (str) – Either ‘buy’ or ‘sell’
	#limitPrice (float) – The price to trigger the market order.
	#stopPrice (float) – The price to trigger the limit or market order.
	#timeInForce (str) – Changes how long the order will be in effect for. ‘gtc’ = good until cancelled. ‘gfd’ = good for the day.
	#extendedHours (Optional[str]) – Premium users only. Allows trading during extended hours. Should be true or false.
	#jsonify (Optional[str]) – If set to False, function will return the request object which contains status code and headers.
	#Returns: Dictionary that contains information regarding the purchase or selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately for fractional shares by specifying the amount in dollars that you want to trade. Good for share fractions up to 6 decimal places. Robinhood does not currently support placing limit, stop, or stop loss orders for fractional trades.
def order_buy_fractional_by_price(symbol, amountInDollars):
	return r.orders.order_buy_fractional_by_price(symbol, amountInDollars, timeInForce = 'gfd', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately for fractional shares by specifying the amount that you want to trade. Good for share fractions up to 6 decimal places. Robinhood does not currently support placing limit, stop, or stop loss orders for fractional trades.
def order_buy_fractional_by_quantity(symbol, quantity):
	return r.orders.order_buy_fractional_by_quantity(symbol, quantity, timeInForce = 'gfd', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a limit order to be executed once a certain price is reached.
def order_buy_limit(symbol, quantity, limitPrice):
	return r.orders.order_buy_limit(symbol, quantity, limitPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately.
def order_buy_market(symbol, quantity):
	return r.orders.order_buy_market(symbol, quantity, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a stop order to be turned into a limit order once a certain stop price is reached.
def order_buy_stop_limit(symbol, quantity, limitPrice, stopPrice):
	return r.orders.order_buy_stop_limit(symbol, quantity, limitPrice, stopPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a stop order to be turned into a market order once a certain stop price is reached.
def order_buy_stop_loss(symbol, quantity, stopPrice):
	return r.orders.order_buy_stop_loss(symbol, quantity, stopPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a trailing stop buy order to be turned into a market order when traling stop price reached.
def order_buy_trailing_stop(symbol, quantity, trailAmount):
	return r.orders.order_buy_trailing_stop(symbol, quantity, trailAmount, trailType = 'percentage', timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately for fractional shares by specifying the amount in dollars that you want to trade. Good for share fractions up to 6 decimal places. Robinhood does not currently support placing limit, stop, or stop loss orders for fractional trades.
def order_sell_fractional_by_price(symbol, amountInDollars):
	return r.orders.order_sell_fractional_by_price(symbol, amountInDollars, timeInForce = 'gfd', extendedHours = False, jsonify = True)
	#Returns Dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately for fractional shares by specifying the amount that you want to trade. Good for share fractions up to 6 decimal places. Robinhood does not currently support placing limit, stop, or stop loss orders for fractional trades.
def order_sell_fractional_by_quantity(symbol, quantity):
	return r.orders.order_sell_fractional_by_quantity(symbol, quantity, timeInForce = 'gfd', priceType = 'bid_price', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a limit order to be executed once a certain price is reached.
def order_sell_limit(symbol, quantity, limitPrice):
	return r.orders.order_sell_limit(symbol, quantity, limitPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a market order to be executed immediately.
def order_sell_market(symbol, quantity):
	return r.orders.order_sell_market(symbol, quantity, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns Dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a stop order to be turned into a limit order once a certain stop price is reached.
def order_sell_stop_limit(symbol, quantity, limitPrice, stopPrice):
	return r.orders.order_sell_stop_limit(symbol, quantity, limitPrice, stopPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a stop order to be turned into a market order once a certain stop price is reached.
def order_sell_stop_loss(symbol, quantity, stopPrice):
	return r.orders.order_sell_stop_loss(symbol, quantity, stopPrice, timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a trailing stop sell order to be turned into a market order when traling stop price reached.
def order_sell_trailing_stop(symbol, quantity, trailAmount):
	return r.orders.order_sell_trailing_stop(symbol, quantity, trailAmount, trailType = 'percentage', timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns dictionary that contains information regarding the selling of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.
	#Returns dictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


#Submits a trailing stop order to be turned into a market order when traling stop price reached.
def order_trailing_stop(symbol, quantity, side, trailAmount):
	return r.orders.order_trailing_stop(symbol, quantity, side, trailAmount, trailType = 'percentage', timeInForce = 'gtc', extendedHours = False, jsonify = True)
	#Returns ictionary that contains information regarding the purchase of stocks, such as the order id, the state of order (queued, confired, filled, failed, canceled, etc.), the price, and the quantity.


"""
Exporting Functions
"""

#Creates a filepath given a directory and file name.
def create_absolute_csv(dir_path, file_name, order_type):
	return r.export.create_absolute_csv(dir_path, file_name, order_type)
	#Returns an absolute file path as a string.


#Write all completed orders to a csv file
def export_completed_stock_orders(dir_path):
	#file_name (Optional[str]) – An optional argument for the name of the file. If not defined, filename will be stock_orders_{current date}
	r.export.export_completed_stock_orders(dir_path, file_name = None)

	
"""
Plot for top panel
"""

def top_panel(ticker):
	# get historical data, default is hourly for the past week
	data = robin_stocks.robinhood.stocks.get_stock_historicals(ticker, interval='hour', span='month')

	prices = []
	times = []
	for datum in data:
	    prices.append(float(datum['close_price']))
	    times.append(datum['begins_at']) # needs better formatting

	plt.plot(range(len(prices)), prices)
	plt.show()
