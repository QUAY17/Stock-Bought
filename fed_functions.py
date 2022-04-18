# requires fredpy package
# requires statsmodels package
import numpy as np
import fredpy as fp
import datetime
import pandas as pd

def enter_api_key():
	key = input("Enter your 32 character API Key: ")
	fp.api_key = '59b76a3e8c24982778e2ae0c69a92996' # hardcoded student account

def get_unemployment_rate():
	'''prints unemployment rate'''
	unemployment = fp.series('UNRATE')
	print("Unemployment Rate: %s%%" % unemployment.data[-1])


def get_gdp():
	gdp = fp.series('gdpc1')
	print("Quarterly GDP (billions): ", gdp.data[-1])

def get_cpi():
	cpi = fp.series('CPIAUCSL')
	diff = ((cpi.data[-1] / cpi.data[-2]) - 1) * 100 
	print("CPI: ", cpi.data[-1])
	print("CPI change since last month: %s%%" % round(diff, 2))


def get_overnight_rate():
	# Specify the API path
	path = 'fred/series/observations'

	# Set observation_date string as today's date
	observation_date = datetime.datetime.today().strftime('%Y-%m-%d')

	# Specify desired parameter values for the API querry; knowing series_id is key!
	parameters = {'series_id':'FEDFUNDS', 'observation_date':observation_date,'file_type':'json'}

	# API request
	r = fp.fred_api_request(api_key=fp.api_key,path=path,parameters=parameters)

	# Return results in JSON format
	results = r.json()

	# Load data, deal with missing values, format dates in index, and set dtype
	data = pd.DataFrame(results['observations'],columns =['date','value'])
	data = data.replace('.', np.nan)
	data['date'] = pd.to_datetime(data['date'])
	data = data.set_index('date')['value'].astype(float)

	print("Fed Overnight rate: %s%%" % data[-1])


def get_interest_rate():
	path = 'fred/series/observations'

	# Set observation_date string as today's date
	observation_date = datetime.datetime.today().strftime('%Y-%m-%d')

	# Specify desired parameter values for the API querry; knowing series_id is key!
	parameters = {'series_id':'INTDSRUSM193N','observation_date':observation_date,'file_type':'json'}

	# API request
	r = fp.fred_api_request(api_key=fp.api_key,path=path,parameters=parameters)

	# Return results in JSON format
	results = r.json()

	# Load data, deal with missing values, format dates in index, and set dtype
	data = pd.DataFrame(results['observations'],columns =['date','value'])
	data = data.replace('.', np.nan)
	data['date'] = pd.to_datetime(data['date'])
	data = data.set_index('date')['value'].astype(float)
	
	print("Fed Interest Rate: %s%%" % data[-1])

