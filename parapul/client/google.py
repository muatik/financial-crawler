# -*- coding: utf8 -*-
from base import CurrencyParity


class Google(CurrencyParity):
    parityURL = "https://www.google.com/finance?q={}"
    parityQuery = "#currency_value > div.sfe-break-bottom-4 > span.pr > span"

    @classmethod
    def extractParity(cls, parityCode):
        parity = super(Google, cls).extractParity(parityCode)
        return parity.split(" ")[0]
