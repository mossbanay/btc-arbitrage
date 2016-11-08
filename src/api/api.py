from api.btce import BTCeMarket
from api.kraken import KrakenMarket

import logging

class MarketAccessFailure(Exception):
    pass

class MarketAPI(object):
    def __init__(self):
        self.markets_loaded = []
        self.log = logging.getLogger(__name__)

        try:
            btce = BTCeMarket()
            self.markets_loaded.append(btce)
        except MarketAccessFailure:
            self.log.error('Unable to connect to BTCe')

        try:
            kraken = KrakenMarket()
            self.markets_loaded.append(kraken)
        except MarketAccessFailure:
            self.log.error('Unable to connect to Kraken')

    def get_bids(self, pair):
        bids = {}

        for market in self.markets_loaded:
            market_name = market.get_name()
            try:
                pair_symbol = pair.get_pair_by_market(market)
                bid = market.get_bid(pair_symbol)
                bids[market_name] = bid
            except MarketAccessFailure:
                raise MarketAccessFailure('Unable to get bid from market {}'.format(market_name))

        return bids
