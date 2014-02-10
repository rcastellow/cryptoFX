from AbstractPlatform import AbstractPlatform
from exchange.ExchangePlugin import ExchangePlugin
from com.pac.cryptofx.algorithm.MeanReversion import MeanReversion
import logging

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

'''
Function: What belongs in the platform: balances, logger, price history
'''
class FXPlatform(AbstractPlatform):
    '''
    classdocs
    '''
    
    logging.basicConfig()
    logger = logging.getLogger()
#     kellyWager = balance * .01

    def __init__(self, config, exchangePluginTypes):
        '''
        Constructor
        '''
        self.config=config
        self.exchangePlugins = []
        for exchangePluginType in exchangePluginTypes:
            self.exchangePlugins.append(ExchangePlugin.factory(exchangePluginType,config))
          
        self.timerInstance = ''
        self.logger.setLevel(logging.DEBUG)

        # Initialize Platform fields     
        self.buyPrices = []
        self.sellPrices = []
        self.balance = {'LTC':10,'USD':0,'BTC':0}     
    
    def logBalance(self,ticker):
        self.logger.debug("balance:")
        self.logger.debug(self.balance['LTC'])
        self.logger.debug(self.balance['USD'])
        self.logger.debug("totalValue USD:")
        totalValueUSD = self.balance['USD'] + (self.balance['LTC'] * ticker['sell'])
        self.logger.debug(totalValueUSD)
        self.logger.debug("totalValue LTC:")
        totalValueLTC = self.balance['LTC'] + (self.balance['USD'] / ticker['buy'])
        self.logger.debug(totalValueLTC)
    
        # Write to history file
        historyField = []
        historyField.append(self.getFormattedCurrentTime())
        historyField.append(ticker['buy'])
        historyField.append(ticker['sell'])
        self.writeToHistoryFile(self.formatCurrentPrice(historyField))
    
    def decisionRules(self):                 
        # TODO: Abstract the MeanReversion into a generic Algorithm module
        meanReversion = MeanReversion(self.config)
        ticker = meanReversion.pollPrice(self.exchangePlugins)
        
        self.buyPrices.append(ticker['buy'])
        self.sellPrices.append(ticker['sell'])
        
        self.balance = meanReversion.trade(self.logger,self.exchangePlugins,ticker,self.balance,
                                           self.buyPrices)
        self.logBalance(ticker)         

        periodicMovingWindow = int(self.config['algorithm.meanReversion.periodicMovingWindow'])
        if (len(self.buyPrices) > 2 * (periodicMovingWindow)):     
            del self.buyPrices[0]
            del self.sellPrices[0]

        
