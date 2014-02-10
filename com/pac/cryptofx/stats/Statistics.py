from numpy import std
import numpy as numpy
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

class Statistics(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
   
    # Uses the past 20 days
    @staticmethod
    def calculateMovingAverage(data, window_size):  
        if (len(data) < window_size): return 
        intervalData = numpy.array(data)[:]
        weights = numpy.ones(int(window_size)) / float(window_size)  # Reset weights if wnating to go exponential, etc
        return numpy.convolve(intervalData, weights, 'valid')
    
    @staticmethod
    def calculateAverage(data):
        priceList = numpy.array(data)[:]
        return reduce(lambda x, y: x + y, priceList) / len(priceList)
    
    @staticmethod
    def calculateStandardDeviation(data,window): 
        if (len(data) < window): return 
        intervalData = numpy.array(data)[:]
        shape = intervalData.shape[:-1] + (intervalData.shape[-1] - window + 1, window)
        strides = intervalData.strides + (intervalData.strides[-1],)
        stdWindow = numpy.lib.stride_tricks.as_strided(intervalData, shape=shape, strides=strides)
        return std(stdWindow, 1)
    
    @staticmethod
    def calculateBolingerBands(movingAverage,standardDeviation):
        lowerBand = movingAverage - 2*standardDeviation
        upperBand = movingAverage + 2*standardDeviation
        return {'lowerBand': lowerBand, 'upperBand' : upperBand}
    
    
