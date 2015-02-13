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


class Google(CurrencyParity):
    parityURL = "https://www.google.com/finance?q={}"
    parityQuery = "#currency_value > div.sfe-break-bottom-4 > span.pr > span"

    @classmethod
    def extractParity(cls, parityCode):
        parity = super(Google, cls).extractParity(parityCode)
        return parity.split(" ")[0]


class Uzmanpara(Stock):
    stockURL = "http://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/{0}/"
    priceQuery = 'div.realTime > span.price-arrow-down'
    volumeQuery = '.realTime table tr td'
    timezone = "Europe/Istanbul"

    @classmethod
    def extractVolume(cls, d):
        return d(cls.volumeQuery)[7].text[1:].replace(".", "")


class Bigpara(Stock):
    timezone = "Europe/Istanbul"
    stockURL = "http://www.bigpara.com/borsa/hisse-detay-bilgileri/{0}/"
    priceQuery = '.piyasaBox .area1'
    volumeQuery = '.newProcessBar li span b'


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


# wall street journal
class TWSJ(Oil):
    timezone = "utc"

    # commodities
    oilURL = "http://quotes.wsj.com/futures/UK/LCOJ5"
    oilQuery = "#mdad_quote_span"


if __name__ == '__main__':
    print("Testing crawlers by fetching the stock ISCTR:")
    # print Uzmanpara.getStock("THYAO")
    # print Bigpara.getStock("THYAO")
    # print MarketWatch.getStock("THYAO")
    # print MarketWatch.getParity("usd-try")
    # print Google.getParity("usd-try")
    print MarketWatch.getParity("eurusd")
    print Google.getParity("eurusd")
    print MarketWatch.getOil()
    print TWSJ.getOil()
