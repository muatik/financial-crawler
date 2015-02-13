# -*- coding: utf8 -*-
from base import Stock, CurrencyParity, Oil


class MarketWatch(Stock, CurrencyParity, Oil):
    timezone = "utc"

    # commodities
    oilURL = "http://www.marketwatch.com/investing/Future"\
        "/BRENT%20CRUDE?countrycode=UK"
    oilQuery = ".lastprice .data.bgLast"

    # parities
    parityURL = "http://www.marketwatch.com/investing/currency/{}"
    parityQuery = ".lastprice .data.bgLast"

    # stocks
    stockURL = "http://www.marketwatch.com/investing/stock/{}"
    priceQuery = '.lastprice .bgLast'
    volumeQuery = '.bgVolume'

    @classmethod
    def formatParityCode(cls, parityCode):
        return "".join(parityCode.split("-"))

    @classmethod
    def extractVolume(cls, d):
        price = cls.extractStockPrice(d)
        volume = d(cls.volumeQuery)[0].text[:-1].replace(".", "")
        return str(float(volume) * float(price) * 10000)
