class Currency(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_currency_by_market(self, market):
        if market.get_name() == 'BTCe':
            return {'btc':'btc',
                    'ltc':'ltc',
                    'eth':'eth',
                    'eur':'eur',
                    'usd':'usd'}[self.symbol]

        elif market.get_name() == 'Kraken':
            return {'btc':'XXBT',
                    'dao':'XDAO',
                    'ltc':'XLTC',
                    'eth':'XETH',
                    'etc':'XETC',
                    'eur':'ZEUR',
                    'gbp':'ZGBP',
                    'jpy':'ZJPY',
                    'cad':'ZCAD',
                    'usd':'ZUSD'}[self.symbol]

class Pair(object):
    def __init__(self, base_currency, transaction_currency):
        if not isinstance(base_currency, Currency):
            raise ValueError('Pair expects a Currency class for the base currency got class {}'.format(type(base_currency)))
        if not isinstance(transaction_currency, Currency):
            raise ValueError('Pair expects a Currency class for the transaction currency got class {}'.format(type(transaction_currency)))

        self.base = base_currency
        self.transaction = transaction_currency

    def get_pair_by_market(self, market):
        base = self.base.get_currency_by_market(market)
        transaction = self.transaction.get_currency_by_market(market)

        if market.get_name() == 'BTCe':
            return '{}_{}'.format(base, transaction)

        elif market.get_name() == 'Kraken':
            return '{}{}'.format(base, transaction)
