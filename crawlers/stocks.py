# -*- coding: utf8 -*-
from pyquery import PyQuery as pq
import arrow


class Stock(object):
    stockURL = None
    priceQuery = None
    volumeQuery = None
    timezone = "Europe/Istanbul"
    minuteSpan = -20

    @classmethod
    def extractPrice(cls, d):
        return d(cls.priceQuery)[0].text

    @classmethod
    def extractVolume(cls, d):
        return d(cls.volumeQuery)[0].text.replace(".", "")

    @classmethod
    def getStock(cls, stockCode):
        """
        returns the price of the given stock as following:
        {"data": "utc date", "price": "4.1"}
        """

        d = pq(url=cls.stockURL.format(stockCode))
        price = cls.extractPrice(d)
        volume = cls.extractVolume(d)

        local = arrow.utcnow().to(cls.timezone)
        priceDate = local.replace(minutes=cls.minuteSpan)

        def makeFloat(v):
            return float(v.replace(',', '.'))

        return {
            "date": priceDate.to('utc'),
            "volume": makeFloat(volume),
            "price": makeFloat(price)
        }


class Uzmanpara(Stock):
    stockURL = "http://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/{0}/"
    priceQuery = '.realTime .price-arrow-up'
    volumeQuery = '.realTime table tr td'
    timezone = "Europe/Istanbul"

    @classmethod
    def extractVolume(cls, d):
        return d(cls.volumeQuery)[7].text[1:].replace(".", "")


class Bigpara(Stock):
    stockURL = "http://www.bigpara.com/borsa/hisse-detay-bilgileri/{0}/"
    priceQuery = '.piyasaBox .area1'
    timezone = "Europe/Istanbul"
    volumeQuery = '.newProcessBar li span b'


class MarketWatch(Stock):
    stockURL = "http://www.marketwatch.com/investing/stock/{}"
    priceQuery = '.lastprice .bgLast'
    timezone = "utc"
    volumeQuery = '.bgVolume'

    @classmethod
    def extractVolume(cls, d):
        price = cls.extractPrice(d)
        volume = d(cls.volumeQuery)[0].text[:-1].replace(".", "")
        return str(float(volume) * float(price) * 10000)

if __name__ == '__main__':
    print("Testing crawlers by fetching the stock ISCTR:")
    print Uzmanpara.getStock("ISCTR")
    # print Bigpara.getStock("THYAO")
    # print MarketWatch.getStock("THYAO")
