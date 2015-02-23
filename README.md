# Financial Crawler
This projects presents some clients which can fetch stock and oil price, currencies and parities from various market web sites.

This is an experimental work about detectiong correlations and causations in stock prices by looking at stock prices, commodities, currencies etc...

## Installation
It is available in pip.
```bash
apt-get install libxml2-dev libxslt1-dev
pip install financialCrawler
```

## Usage
```python
from financialCrawler import clients

>>> print ("\nfetching Facebook's stock price from marketwatch.com")
>>> print clients.Uzmanpara.getStock("FB")
{'date': <Arrow [2015-02-23T15:08:43.631594+00:00]>,
 'price': 79.18,
 'volume': 455285000.0}
>>> print clients.Google.getParitiy("eurusd")
{'date': <Arrow [2015-02-23T15:30:09.162236+00:00]>, 'parity': 1.1338}
```

For more examples and documentation please have a look at [wiki pages](https://github.com/muatik/financial-crawler/wiki).