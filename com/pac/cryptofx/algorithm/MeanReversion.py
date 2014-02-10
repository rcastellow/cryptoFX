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

class MeanReversion():
    '''
    classdocs
    '''
    
    def __init__(self,config):
        
        self.currencyPair = config['algorithm.meanReversion.currencyPair']
        self.periodicMovingWindow = int(config['algorithm.meanReversion.periodicMovingWindow'])
        
        '''
        Constructor
        '''
          
    def buyOrSellDecision(self,ticker,buyPrices,balances,logger):
        currentSellPrice = ticker['sell']  # TODO: Test between buy or sell price
        currentBuyPrice = ticker['buy']

        buyMovingAverage = Statistics.calculateMovingAverage(buyPrices, self.periodicMovingWindow)  # 20 interval moving average 
         
        logger.debug(buyPrices)
        logger.debug(buyMovingAverage)
        
                # Run rules on current prices
        if (len(buyPrices) > self.periodicMovingWindow):
            standardDeviation = Statistics.calculateStandardDeviation(buyPrices, self.periodicMovingWindow)  # 2 interval moving stddevs
            bolingerBands = Statistics.calculateBolingerBands(buyMovingAverage, standardDeviation)                                      
            upperBand = bolingerBands['upperBand'][-1]
            lowerBand = bolingerBands['lowerBand'][-1]
    
            logger.debug('Lower Band:')
            logger.debug(lowerBand)
            logger.debug('Upper Band:')
            logger.debug(upperBand)
            
            if ((currentBuyPrice > upperBand) and (balances['balanceLTC'] > (0.1 * currentSellPrice))):
                logger.debug("SELL-SELL-SELL!!")
                return 'sell'
            elif ((currentBuyPrice < lowerBand) and (balances['balanceUSD'] > (0.1 * currentBuyPrice))):
                logger.debug("BUY-BUY-BUY!!")
                return 'buy'
            else:
                return 'continue'
            
    def pollPrice(self, exchangePlugins):
        return exchangePlugins[0].getCurrentPrice(self.currencyPair)        
           
    def trade(self,logger,exchangePlugins,ticker, balance,buyPrices):
        
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
                

            