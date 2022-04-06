# requires yfinance
import yfinance as yf

def get_margins(ticker):
	'''returns margin percentages for a given company'''
	data = yf.Ticker(ticker)
	margin_keys = ['profitMargins', 'grossMargins', 'operatingMargins']
	for key in margin_keys:
		print("%s: %s%%" % (key, str(round(100 * data.info[key], 1))))


def get_forwards(ticker):
	'''returns forward EPS and PE'''
	data = yf.Ticker(ticker)
	forward_keys = ['forwardEps', 'forwardPE']
	for key in forward_keys:
		print('%s: %s' % (key, round(data.info[key], 2)))
