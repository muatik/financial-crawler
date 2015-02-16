# -*- coding: utf8 -*-
from base import Stock


class Uzmanpara(Stock):
    stockURL = "http://uzmanpara.milliyet.com.tr/borsa/hisse-senetleri/{0}/"
    priceQuery = '.realTime > .price-arrow-down, .realTime > .price-arrow-up'
    volumeQuery = '.realTime table tr td'
    timezone = "Europe/Istanbul"

    @classmethod
    def extractVolume(cls, d):
        return d(cls.volumeQuery)[7].text[1:].replace(".", "")
