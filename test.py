import robin_stocks_functions as rsf
import fundamentals_functions as ff
import fed_functions as fed

# testing some robin_stocks functions:
#rsf.login("jminniecc@gmail.com","hgPSznGL5STp8QK")
#rsf.plot_hourly_historical('TSLA')
#rsf.get_spot_price('TSLA')

# testing some fundamentals functions:
#ff.get_margins('TSLA')
#ff.get_forwards('TSLA')

# testing FRED functions:
fed.enter_api_key()
fed.get_unemployment_rate()
fed.get_gdp()
fed.get_cpi()
fed.get_overnight_rate()
fed.get_interest_rate()
