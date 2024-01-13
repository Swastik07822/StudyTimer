import time

class Time:
    def __init__(self):
        self.start = time.strftime( "%H:%M:%S",time.localtime())
        self.end = None
    def started(self):
        return self.start
    def finished(self):
        self.end = time.strftime( "%H:%M:%S",time.localtime())
        return self.end
    

        



        
