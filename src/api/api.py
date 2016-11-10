from api.btce import BTCeMarket
from api.kraken import KrakenMarket
from api.poloniex import PoloniexMarket
from api.ccex import CCexMarket

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

        try:
            polo = PoloniexMarket()
            self.markets_loaded.append(polo)
        except MarketAccessFailure:
            self.log.error('Unable to connect to Poloniex')

        try:
            ccex = CCexMarket()
            self.markets_loaded.append(ccex)
        except MarketAccessFailure:
            self.log.error('Unable to connect to C-Cex')


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

    def get_asks(self, pair):
        asks = {}

        for market in self.markets_loaded:
            market_name = market.get_name()
            try:
                pair_symbol = pair.get_pair_by_market(market)
                ask = market.get_ask(pair_symbol)
                asks[market_name] = ask
            except MarketAccessFailure:
                raise MarketAccessFailure('Unable to get ask from market {}'.format(market_name))

        return asks
