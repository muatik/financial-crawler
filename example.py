# -*- coding: utf8 -*-
from financialCrawler import clients

print("\nTesting crawlers by fetching the stock price of THYAO:")

print ("\nfetching THYAO stock price from uzmanpara.com")
print clients.Uzmanpara.getStock("THYAO")

print ("\nfetching THYAO stock price from bigpara.com")
print clients.Bigpara.getStock("THYAO")

print ("\nfetching THYAO stock price from MarketWatch.com")
print clients.MarketWatch.getStock("THYAO")

print ("\nfetching euro-usd parity from MarketWatch.com")
print clients.MarketWatch.getParity("eurusd")

print ("\nfetching euro-usd parity from Google.com")
print clients.Google.getParity("eurusd")

print ("\nfetching usd-jpy parity from MarketWatch.com")
print clients.MarketWatch.getParity("usdjpy")

print ("\nfetching brent oil price from MarketWatch.com")
print clients.MarketWatch.getOil()

print ("\nfetching brent oil price from thewallstreetjournal.com")
print clients.TWSJ.getOil()
