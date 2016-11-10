import requests

class PoloniexBadPairNameException(Exception):
    pass

class PoloniexMarket(object):
    def __init__(self):
        self.fee = 0.002
        self.public_api_url = 'https://poloniex.com/public?command='

    def get_name(self):
        return 'Poloniex'

    def get_ticker(self, pair):
        req_url = self.public_api_url + 'returnTicker'

        req = requests.get(req_url)

        data = req.json()

        if pair not in data:
            raise BTCeBadPairNameException('Unable to find pair {} on Poloniex'.format(pair))

        return data[pair]

    def get_bid(self, pair):
        ticker = self.get_ticker(pair)

        return float(ticker['lowestAsk'])

    def get_ask(self, pair):
        ticker = self.get_ticker(pair)

        return float(ticker['highestBid'])
