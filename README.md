# SWE-326 Stock Bought Python Project

The motivation for this project follows an entry-level consumer’s desire to begin their investment
venture and broaden their financial horizons. Specifically, the project involves, and was incited by,
Robinhood: A financial services company whose claim to fame resides in its pioneered—now widely
adopted—commission-free investing. This key feature makes Robinhood the de facto medium for an
individual interested in investing in stocks, crypto, IPOs, etc.—without the overhead of traditional
investing. Staying in-line with Robinhood’s appeal to the entry-level investor, this project aims to create
tools for such an investor to create, test, and automatically implement their given trading scheme on
Robinhood. Our project is proposed to be, at its core, a toolkit to aid algorithmic trading—both in its
production and implementation.

Statement of Proposal: We propose to build a software toolkit that is meant to be used as an extension to
Robinhood’s API. Our tools include the additional functionality of aggregating external data, editing stock price target models, backtesting tools, and automated execution of
certain actions on Robinhood—namely buy/sell orders.


# Please see requirements.txt for installation instructions, also posted below:

Requirement packages for the project <br>
Running 'pip install -r requirements.txt' will install everything here <br>

robin-stocks==2.1.0 <br>
PyQt5==5.15.4 <br>
PyQt5-sip==12.9.0 <br>
PyQtWebEngine==5.15.4 <br>
yfinance==0.1.70 <br>
matplotlib==3.4.3 <br>
fredpy==3.2.6 <br>
statsmodels==0.13.2 <br>
backtrader==1.9.76.123 <br>
pyqtgraph==0.11.1 <br>
python-dateutil==2.8.2 <br>
requests==2.27.1 <br>

For Ubuntu: <br>
sudo apt-get build-dep qt5-default <br>
sudo apt-get install libxcb-xinerama0-dev <br>
