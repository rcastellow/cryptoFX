from apscheduler.scheduler import Scheduler

'''
Created on Jan 26, 2014

@author: RobCastellow
'''

class TimerManager:
    '''
    classdocs
    '''


    def __init__(self,currentPlatform):
        '''
        Constructor
        '''
        self.currentPlatform = currentPlatform
        
        
    def scheduledJob1(self):        
        self.currentPlatform.execute()
          
    
    def runScheduler(self, interval, periodicMovingWindow):
        self.currentPlatform.logger.info("Started Scheduler.")
        sched = Scheduler()
        sched.add_interval_job(self.scheduledJob1, minutes=interval)
        sched.start() 
        
        while True:
            pass
        self.logger.info("Finished Scheduler.")