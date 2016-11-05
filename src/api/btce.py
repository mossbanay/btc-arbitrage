import requests, logging

class BTCeBadPairNameException(Exception):
    pass

class BTCeMarket(object):
    def __init__(self):
        self.fee = 0.002
        self.api_url = 'https://btc-e.com/api/3/'

    def get_name(self):
        return 'BTCe'

    def get_ticker(self, pair):
        req_url = self.api_url + 'ticker/{}'.format(pair)

        req = requests.get(req_url)

        data = req.json()

        if 'error' in data.keys():
            raise BTCeBadPairNameException('Unable to find pair {} on BTCe'.format(pair))

        return data

    def get_bid(self, pair):
        ticker = self.get_ticker(pair)

        return ticker[pair]['buy']

    def get_ask(self, pair):
        ticker = self.get_ticker(pair)

        return ticker[pair]['sell']
