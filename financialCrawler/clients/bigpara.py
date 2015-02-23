# -*- coding: utf8 -*-
from base import Stock


class Bigpara(Stock):
    timezone = "Europe/Istanbul"
    stockURL = "http://www.bigpara.com/borsa/hisse-detay-bilgileri/{0}/"
    priceQuery = '.piyasaBox .area1'
    volumeQuery = '.newProcessBar li span b'
