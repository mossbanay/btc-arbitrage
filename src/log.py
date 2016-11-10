from api.api import MarketAPI
from api.currency import Currency, Pair
import time, os.path


PAIRS = [Pair(Currency('btc'), Currency('usd')),
         Pair(Currency('eth'), Currency('btc')),
         Pair(Currency('ltc'), Currency('btc'))]

def main():

    cur_dir = os.path.dirname(os.path.realpath(__file__))

    if not os.path.exists(os.path.join(cur_dir, 'logs/')):
        os.makedirs(os.path.join(cur_dir, 'logs/'))

    api = MarketAPI()

    for pair in PAIRS:

        bids = api.get_bids(pair)
        asks = api.get_asks(pair)

        logfile_name = os.path.join(cur_dir, 'logs/' + pair.get_symbol() + '.csv')

        if not os.path.isfile(logfile_name):
            with open(logfile_name, 'w'):
                pass

        with open(logfile_name, 'a') as f:
            for market in bids.keys():
                f.write('{},{},{},{}\n'.format(int(time.time()),
                                     market,
                                     'bid',
                                     bids[market]))
            for market in asks.keys():
                f.write('{},{},{},{}\n'.format(int(time.time()),
                                     market,
                                     'ask',
                                     asks[market]))


if __name__ == '__main__':
    main()
