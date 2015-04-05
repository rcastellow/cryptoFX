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
import unittest
from com.pac.cryptofx.exchange.bitfinex.BitfinexExchangePlugin import BitfinexExchangePlugin 
from configobj import ConfigObj
from mock import MagicMock

class Test(unittest.TestCase):

    apiKey = 's87hi6OhcYFDRnPHXzhTQE9GddWC1R1VkEG79f53qvP'
    apiSecret = '4bZefLiSh0O92QcuwZQzm46c7Dy0lycvJPFW387UbUh'
    config = ConfigObj('cryptofxTest.properties')

    def testName(self):
        pass
    
    def testGetTicker(self):
        bfep = BitfinexExchangePlugin(self.config)
        ticker = bfep.getTicker('ltcbtc')
        self.assertNotEqual('', ticker['ask'])
        self.assertNotEqual('', ticker['timestamp'])
        self.assertNotEqual('', ticker['bid'])
        self.assertNotEqual('', ticker['last_price'])
        self.assertNotEqual('', ticker['mid'])
        
    def testGetToday(self):
        bfep = BitfinexExchangePlugin(self.config)
        ticker = bfep.getToday('ltcbtc')
        self.assertNotEqual('', ticker['low'])
        self.assertNotEqual('', ticker['high'])
        self.assertNotEqual('', ticker['volume'])

    def testGetStats(self):
        bfep = BitfinexExchangePlugin(self.config)
        ticker = bfep.getStats('ltcbtc')
        self.assertEquals(1, ticker[0]['period'])
        self.assertNotEqual('', ticker[0]['volume'])
        self.assertEquals(7, ticker[1]['period'])
        self.assertNotEqual('', ticker[1]['volume'])
        self.assertEquals(30, ticker[2]['period'])
        self.assertNotEqual('', ticker[2]['volume'])
        
    def testGetLendbook(self):
        bfep = BitfinexExchangePlugin(self.config)
        params = {}
        params['limit_asks']=2
        params['limit_bids']=2
        ticker = bfep.getLendbook('ltc',params)
#         self.assertNotEqual('', ticker['bids'][0]['timestamp'])
#         self.assertNotEqual('', ticker['bids'][0]['rate'])
#         self.assertNotEqual('', ticker['bids'][0]['amount'])
#         self.assertNotEqual('', ticker['bids'][0]['period'])
#         self.assertNotEqual('', ticker['asks'][0]['timestamp'])
#         self.assertNotEqual('', ticker['asks'][0]['rate'])
#         self.assertNotEqual('', ticker['asks'][0]['amount'])
#         self.assertNotEqual('', ticker['asks'][0]['period'])
                        
    def testGetBook(self):
        bfep = BitfinexExchangePlugin(self.config)
        params = {}
        params['limit_asks']=2
        params['limit_bids']=2
        ticker = bfep.getLendbook('ltc',params)
#         self.assertNotEqual('', ticker['bids'][0]['timestamp'])
#         self.assertNotEqual('', ticker['bids'][0]['rate'])
#         self.assertNotEqual('', ticker['bids'][0]['amount'])
#         self.assertNotEqual('', ticker['bids'][0]['period'])
#         self.assertNotEqual('', ticker['asks'][0]['timestamp'])
#         self.assertNotEqual('', ticker['asks'][0]['rate'])
#         self.assertNotEqual('', ticker['asks'][0]['amount'])
#         self.assertNotEqual('', ticker['asks'][0]['period']) 
        
    def testGetTrades(self):
        self.assertEquals(1, 1)
        
    def testGetLends(self):
        self.assertEquals(1, 1)
                
    def testGetSymbols(self):
        self.assertEquals(1, 1)
                
    def testNewOrder(self):
        self.assertEquals(1, 1)
                
    def testNewMultiOrders(self):
        self.assertEquals(1, 1)
                
    def testCancelOrder(self):
        self.assertEquals(1, 1)
        
    def testCancelMultiOrders(self):
        self.assertEquals(1, 1)
        
    def testCancelAllActiveOrders(self):
        self.assertEquals(1, 1)        
        
    def testCancelReplaceOrder(self):
        self.assertEquals(1, 1) 
               
    def testOrderStatus(self):
        self.assertEquals(1, 1)
                
    def testGetActiveOrders(self):
        bfep = BitfinexExchangePlugin(self.config)
        bfep.apiKey = self.apiKey
        bfep.apiSecret = self.apiSecret
        ticker = bfep.getActiveOrders()
        print ticker
        self.assertEquals(1, ticker[0]['period'])
        
    def testActivePositions(self):
        self.assertEquals(1, 1)
        
    def testClaimPosition(self):
        self.assertEquals(1, 1)
                
    def testPastTrades(self):
        self.assertEquals(1, 1)        
        
    def testNewOffer(self):
        self.assertEquals(1, 1)
                
    def testCancelOffer(self):
        self.assertEquals(1, 1)
                
    def testOfferStatus(self):
        self.assertEquals(1, 1)
                
    def testActiveOffers(self):
        self.assertEquals(1, 1)
                
    def testActiveCredits(self):
        bfep = BitfinexExchangePlugin(self.config)
        bfep.apiKey = self.apiKey
        bfep.apiSecret = self.apiSecret
        bfep.getActiveCredits = MagicMock(return_value=[])
        credit = bfep.getActiveCredits()
        self.assertEqual([], credit)
                
    def testWalletBalances(self):
        bfep = BitfinexExchangePlugin(self.config)
        bfep.apiKey = self.apiKey
        bfep.apiSecret = self.apiSecret
        balances = bfep.getWalletBalances()
        print balances
        self.assertEquals(1, balances[0]['period'])      
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()