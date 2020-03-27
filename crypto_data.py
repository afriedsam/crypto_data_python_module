import requests
import pandas as pd

def crypto_current(ticker = "BTC", fiat = "USD"):
	"""
	Use this function to aquire current price of a given cryptocurrency
	Call: crypto_current()
	Parameters:
		ticker(which cryptocurrency)
			(BTC for Bitcoin, ETH for ethermeum, etc.)
		fiat(base currency)
			(USD for US dollars, EUR for Euro, etc.)
	"""
	url = ("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(ticker,fiat))
	data = requests.get(url).json()
	return data[fiat]

def crypto_historical_hour(ticker = 'BTC', fiat = "USD", time = 1):
	"""
	Use this function to aquire historical price data from the last 24 hours
	Call: crypto_historical_hour()
	Parameters:
		ticker(which cryptocurrency)
			(BTC for Bitcoin, ETH for ethermeum, etc.)
		fiat(base currency)
			(USD for US dollars, EUR for Euro, etc.)
		time(what price you would like to pull in)
			(if price from 1 hour ago: time = 1, if price from 2 hours ago: time = 2, etc.)
	"""
	historicalURL = "https://min-api.cryptocompare.com/data/v2/histohour?fsym={}&tsym={}&limit=25".format(ticker, fiat)
	historicalData = requests.get(historicalURL)
	ipdata = historicalData.json()
	dataFrame = pd.DataFrame(ipdata['Data']['Data'])
	historicalCloseData = []
	for closeColumn in dataFrame['close']:
	    historicalCloseData.append(closeColumn)
	return historicalCloseData[24-time]

def crypto_historical_day(ticker = 'BTC', fiat = 'USD', day = 1):
	"""
	Use this function to aquire historical price data from the last 30 Days
	Call: crypto_historical_hour()
	Parameters:
		ticker(which cryptocurrency)
			(BTC for Bitcoin, ETH for ethermeum, etc.)
		fiat(base currency)
			(USD for US dollars, EUR for Euro, etc.)
		day(from which day would you like to aquire the price)
			(if price from 1 day ago: day = 1, if price from 15 days ago: day = 15, etc.)
	"""
	historicalURL = "https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym={}&limit=31".format(ticker, fiat)
	historicalData = requests.get(historicalURL)
	ipdata = historicalData.json()
	dataFrame = pd.DataFrame(ipdata['Data']['Data'])
	historicalCloseData = []
	for closeColumn in dataFrame['close']:
	    historicalCloseData.append(closeColumn)
	return historicalCloseData[30-day]