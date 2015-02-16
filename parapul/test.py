# -*- coding: utf8 -*-
from clients import *

if __name__ == '__main__':
    print("Testing crawlers by fetching the stock ISCTR:")
    print Uzmanpara.getStock("THYAO")
    print Bigpara.getStock("THYAO")
    print MarketWatch.getStock("THYAO")
    print MarketWatch.getParity("usd-try")
    print Google.getParity("usdtry")
    print MarketWatch.getParity("eurusd")
    print Google.getParity("eurusd")
    print MarketWatch.getOil()
    print TWSJ.getOil()
