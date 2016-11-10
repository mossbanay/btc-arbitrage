class Currency(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

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

        elif market.get_name() == 'Poloniex':
            return {'btc':'BTC',
                    'dao':'DAO',
                    'ltc':'LTC',
                    'eth':'ETH',
                    'etc':'ETC',
                    'xmr':'XMR',
                    'zec':'ZEC',
                    'fct':'FCT',
                    'xrp':'XRP',
                    'rep':'REP',
                    'doge':'DOGE',
                    'usd':'USDT'}[self.symbol]

        elif market.get_name() == 'C-Cex':
            return {'btc':'btc',
                    'ltc':'ltc',
                    'eth':'eth',
                    'etc':'etc',
                    'doge':'doge',
                    'usd':'usd'}[self.symbol]



class Pair(object):
    def __init__(self, base_currency, transaction_currency):
        if not isinstance(base_currency, Currency):
            raise ValueError('Pair expects a Currency class for the base currency got class {}'.format(type(base_currency)))
        if not isinstance(transaction_currency, Currency):
            raise ValueError('Pair expects a Currency class for the transaction currency got class {}'.format(type(transaction_currency)))

        self.base = base_currency
        self.transaction = transaction_currency

    def get_symbol(self):
        return self.base.get_symbol() + self.transaction.get_symbol()

    def get_pair_by_market(self, market):
        base = self.base.get_currency_by_market(market)
        transaction = self.transaction.get_currency_by_market(market)

        if market.get_name() == 'BTCe':
            return '{}_{}'.format(base, transaction)

        elif market.get_name() == 'Kraken':
            return '{}{}'.format(base, transaction)

        elif market.get_name() == 'Poloniex':
            return '{}_{}'.format(transaction, base)

        elif market.get_name() == 'C-Cex':
            return '{}-{}'.format(base, transaction)
