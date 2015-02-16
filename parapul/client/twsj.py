# -*- coding: utf8 -*-
from base import Oil


# wall street journal
class TWSJ(Oil):
    timezone = "utc"

    # commodities
    oilURL = "http://quotes.wsj.com/futures/UK/LCOJ5"
    oilQuery = "#mdad_quote_span"
