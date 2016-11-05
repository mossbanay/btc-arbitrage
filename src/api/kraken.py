import requests, logging


class KrakenBadPairNameException(Exception):
    pass

class KrakenMarket(object):
    def __init__(self):
        self.fee = 0.0026
        self.api_url = 'https://api.kraken.com/0/public/'

    def get_name(self):
        return 'Kraken'

    def get_ticker(self, pair):
        req_url = self.api_url + 'Ticker'

        params = {
            'pair':pair
        }

        req = requests.get(url=req_url, params=params)

        data = req.json()

        if data['error']:
            raise KrakenBadPairNameException('Unable to find pair {} on Kraken'.format(pair))

        return data

    def get_bid(self, pair):
        ticker = self.get_ticker(pair)

        return ticker['result'][pair]['a'][0]

    def get_ask(self, pair):
        ticker = self.get_ticker(pair)

        return ticker['result'][pair]['b'][0]
