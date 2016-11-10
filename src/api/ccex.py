import requests

class CCexBadPairNameException(Exception):
    pass

class CCexMarket(object):
    def __init__(self):
        self.fee = 0.002
        self.public_api_url = 'https://c-cex.com/t/api_pub.html?a='

    def get_name(self):
        return 'C-Cex'

    def get_ticker(self, pair):
        req_url = 'https://c-cex.com/t/{}.json'.format(pair)

        req = requests.get(req_url)

        data = req.json()

        if 'ticker' not in data:
            raise CCexBadPairNameException('Unable to find pair {} on C-Cex'.format(pair))

        return data['ticker']

    def get_bid(self, pair):
        ticker = self.get_ticker(pair)

        return ticker['sell']

    def get_ask(self, pair):
        ticker = self.get_ticker(pair)

        return ticker['buy']
