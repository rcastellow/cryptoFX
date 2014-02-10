from com.pac.cryptofx.exchange.ExchangePlugin import ExchangePlugin
from api import api
'''
Created on February 6, 2014

@author: RobCastellow

Copyright (c) 2014 PAC Enterprises, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

class KrakenExchangePlugin(ExchangePlugin):
    '''
    classdocs
    '''

    def getCurrentPrice(self,currencyPair):
        krkApi = api()
        krakenTicker = krkApi.query_public('Ticker', {'pair':currencyPair})
        result = krakenTicker['result'][currencyPair]
        ticker = {}
        ticker['buy'] = float(result['b'][0])
        ticker['sell'] = float(result['a'][0])
        return ticker
        
    def tradeCurrency(self,currencyPair, type, price):
        krkApi = api()
        limitPrice = price + 0.01
        req = {'pair':currencyPair, 'type':type, 'ordertype':'limit', 'price': limitPrice}
        krackenOrder = krkApi.query_private('AddOrder', req)
        print krackenOrder['description']
        print krackenOrder['txid']
        print self.config['exchange.kraken.username']
        return krackenOrder
    