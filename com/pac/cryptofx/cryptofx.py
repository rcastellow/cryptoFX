from FXPlatform import FXPlatform
from timer.TimerManager import TimerManager
from configobj import ConfigObj

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

if __name__ == '__main__':
    pass

# This is the client that will configure the following objects:
# 1. the platform
# 1.5 the exchange
# 2. the timer object
# 3. the currency
# 4. the algorithm (which will include the buy/sell rule set)
# 5. the logger
# 
# Need unit tests!!!

# Initialize Properties file
config = ConfigObj('cryptofx.properties')

#  Use BTC-e exchange APIs
exchangePlugins = ["KrakenExchangePlugin"]
fxCoinPlatform = FXPlatform(config,exchangePlugins)

#btce should use ltc_usd
timerManager = TimerManager(fxCoinPlatform)

interval=int(config['scheduler.interval'])
periodicMovingWindow=int(config['scheduler.periodicMovingWindow'])
timerManager.runScheduler('XLTCZUSD',interval,periodicMovingWindow)

