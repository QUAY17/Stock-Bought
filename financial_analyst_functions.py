# requires yfinance
import yfinance as yf

def get_margins(ticker):
	'''returns margin percentages for a given company'''
	data = yf.Ticker(ticker)
	margin_keys = ['profitMargins', 'grossMargins', 'operatingMargins']
	return data.info[margin_keys[0]], data.info[margin_keys[1]], data.info[margin_keys[2]]


def get_forwards(ticker):
	'''returns forward EPS and PE'''
	data = yf.Ticker(ticker)
	forward_keys = ['forwardEps', 'forwardPE']
	return data.info[forward_keys[0]], data.info[forward_keys[1]]	
