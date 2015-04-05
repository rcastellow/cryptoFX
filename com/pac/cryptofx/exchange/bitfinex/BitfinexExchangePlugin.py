from com.pac.cryptofx.exchange.ExchangePlugin import ExchangePlugin

'''
Created on March 14, 2014

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
import base64
import hashlib
import httplib
import hmac
import json
import time
import urllib

class BitfinexExchangePlugin(ExchangePlugin):
    '''
    classdocs
    '''
    
    apiKey = ''
    apiSecret = ''
    waitForNonce = False
    
    def signature(self, params):
        return hmac.new(self.apiSecret, params, digestmod=hashlib.sha384).hexdigest()
    
    def nonce(self):
        if self.waitForNonce: time.sleep(1)
        self.nonceV = str(time.time()).split('.')[0]

    def post(self, apiKey, apiSecret, request, params={}, waitForNonce=False):
        self.nonce()
        params['nonce'] = str(self.nonceV)
        params['request'] = "/v1/" + request
        jsonObject = json.dumps(params)
        params = base64.standard_b64encode(jsonObject);
        headers = {"X-BFX-APIKEY" : self.apiKey,
                   "X-BFX-SIGNATURE" : self.signature(params),
                   "X-BFX-PAYLOAD" : params}
        httpConnector = httplib.HTTPSConnection("api.bitfinex.com")
        httpConnector.request("POST", "/v1/" + request, params, headers)
        response = httpConnector.getresponse()
        data = json.load(response)
        httpConnector.close()
        return data

    def get(self, path, params=''):
        httpConnection = httplib.HTTPSConnection("api.bitfinex.com")
        params = urllib.urlencode(params)
        if params != "":
            params = '?' + params
        httpConnection.request("GET", "/v1/" + path + params)
        response = httpConnection.getresponse()
        data = json.load(response)
        httpConnection.close()
        return data

    def getTicker(self, symbol):
        path = 'ticker/'
        path += symbol
        return self.get(path)
    
    def getToday(self, symbol):
        path = 'today/'
        path += symbol
        return self.get(path)
    
    def getStats(self, symbol):
        path = 'stats/'
        path += symbol
        return self.get(path)

    def getLendbook(self, currency, params):
        path = 'lendbook/'
        path += currency
        return self.get(path, params)
    
    def getBook(self, currency, params):
        path = 'book/'
        path += currency
        return self.get(path, params)   
    
    def getTrades(self):
        return
        
    def getLends(self):
        return
        
    def getSymbols(self):
        return
        
    def newOrder(self):
        return
        
    def newMultiOrders(self):
        return
        
    def cancelOrder(self):
        return
        
    def cancelMultiOrders(self):
        return
        
    def cancelAllActiveOrders(self):
        return
        
    def cancelReplaceOrder(self):
        return
        
    def getOrderStatus(self):
        return
        
    def getActiveOrders(self):
        path = 'orders'
        return self.post(self.apiKey, self.apiSecret, path)
                
    def getActivePositions(self):
        return
        
    def claimPosition(self):
        return
        
    def getPastTrades(self):
        return
        
    def newOffer(self):
        return
        
    def cancelOffer(self):
        return
        
    def getOfferStatus(self):
        return
        
    def getActiveOffers(self):
        return
        
    def getActiveCredits(self):
        path = 'credits'
        return self.post(self.apiKey, self.apiSecret, path)
        
    def getWalletBalances(self):
        path = 'balances'
        return self.post(self.apiKey, self.apiSecret, path)
    
