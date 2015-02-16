# -*- coding: utf8 -*-
from pyquery import PyQuery as pq
import arrow


def makeFloat(v):
    return float(v.replace(',', '.'))


class Oil(object):
    oilURL = None
    oilQuery = None
    timezone = "utc"
    minuteSpan = -1

    @classmethod
    def extractOil(cls, d):
        try:
            return d(cls.oilQuery)[0].text
        except Exception, e:
            raise Exception("oil price cannot be extracted. " + e.message)

    @classmethod
    def getOil(cls):
        """
        returns the oil price:
        {"data": "utc date", "price": "4.1"}
        """

        d = pq(url=cls.oilURL)
        price = cls.extractOil(d)

        return {
            "date": arrow.utcnow(),
            "price": makeFloat(price)
        }


class CurrencyParity(object):
    parityURL = None
    parityQuery = None
    timezone = "Europe/Istanbul"
    minuteSpan = -1

    @classmethod
    def formatParityCode(cls, parityCode):
        return parityCode

    @classmethod
    def extractParity(cls, d):
        try:
            return d(cls.parityQuery)[0].text
        except Exception, e:
            raise Exception("parity cannot be extracted. " + e.message)

    @classmethod
    def getParity(cls, parityCode):
        """
        returns the value of the parity given as "usd-try":
        {"data": "utc date", "price": "4.1"}
        """

        parityCode = cls.formatParityCode(parityCode)
        d = pq(url=cls.parityURL.format(parityCode))
        parity = cls.extractParity(d)

        local = arrow.utcnow().to(cls.timezone)
        priceDate = local.replace(minutes=cls.minuteSpan)

        return {
            "date": priceDate.to('utc'),
            "parity": makeFloat(parity)
        }


class Stock(object):
    stockURL = None
    priceQuery = None
    volumeQuery = None
    timezone = "Europe/Istanbul"
    minuteSpan = -20

    @classmethod
    def formatStockCode(cls, stockCode):
        return stockCode

    @classmethod
    def extractStockPrice(cls, d):
        try:
            return d(cls.priceQuery)[0].text
        except Exception, e:
            raise Exception("price cannot be extracted. " + e.message)

    @classmethod
    def extractVolume(cls, d):
        try:
            return d(cls.volumeQuery)[0].text.replace(".", "")
        except Exception, e:
            raise Exception("volume cannot be extracted. " + e.message)

    @classmethod
    def getStock(cls, stockCode):
        """
        returns the price of the given stock as following:
        {"data": "utc date", "price": "4.1"}
        """

        stockCode = cls.formatStockCode(stockCode)
        d = pq(url=cls.stockURL.format(stockCode))
        price = cls.extractStockPrice(d)
        volume = cls.extractVolume(d)

        local = arrow.utcnow().to(cls.timezone)
        priceDate = local.replace(minutes=cls.minuteSpan)

        return {
            "date": priceDate.to('utc'),
            "volume": makeFloat(volume),
            "price": makeFloat(price)
        }
