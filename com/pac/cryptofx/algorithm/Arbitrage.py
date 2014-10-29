from com.pac.cryptofx.stats.Statistics import Statistics

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

class Arbitrage():
    '''
    classdocs
    '''
    
    def __init__(self,config):
        '''
        Constructor
        '''
        self.config = config 
          
    def buyOrSellDecision(self,ticker,buyPrices,balances,logger):
        currentSellPrice = ticker['sell']  # TODO: Test between buy or sell price
        currentBuyPrice = ticker['buy']

    def pollPrices(self, exchangePlugin):
        
        # Had to extract currency pairs from the plugin name since
        # each exchange may be different 
        pluginName = exchangePlugin.__class__.__name__
        currencyPairPropertyName =  'algorithm.arbitrage.' 
        currencyPairPropertyName += pluginName
        currencyPairPropertyName += '.currencyPair'
        currencyPair = self.config[currencyPairPropertyName]
        
        return exchangePlugin.getCurrentPrice(currencyPair)        
           
    def trade(self,logger,exchangePlugins,ticker, balance,buyPrices):
        
        #We need to do the following
        # 1. Determine the spreads
        # 2. Find the max spread
        # 3. Buy the low.. sell the high
        # 4. Transfer from high cost exchange to low cost exchange
        # 5. Repeat 1-4
        
        if (self.buyOrSellDecision(ticker,buyPrices,balance,logger) == 'sell'):
            logger.debug("SELL-SELL-SELL!!") #TODO: Hook into buy/seel module
            exchangePlugins[0].tradeCurrency()
            balance['USD'] = balance['USD'] + (0.1 * ticker['sell'])
            balance['LTC'] = balance['LTC'] - 0.1
        elif (self.buyOrSellDecision(ticker,buyPrices,balance,logger) == 'buy'):
            logger.debug("BUY-BUY-BUY!!") #TODO: Link into buy/sell module
            exchangePlugins[0].tradeCurrency()
            balance['USD'] = balance['USD'] - (0.1 * ticker['buy'])
            balance['LTC'] = balance['LTC'] + 0.1
        
        return balance
                

            