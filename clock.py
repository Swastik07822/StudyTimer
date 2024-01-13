import time
min,sec,hr = 0,0,0
flag = 0

class clock:
    def __init__(self):
        self.flag = True
        self.hr = 0
        self.min = 0
        self.sec = 0
    def show_time(self):
        while self.flag:
            if self.sec < 59 and self.min <=59 and self.hr <=23:
                self.sec += 1
            elif self.sec == 59 and self.min <59 and self.hr <23:
                self.sec = 0
                self.min += 1
            elif self.sec == 59 and self.min == 59 and self.hr <23:
                self.hr += 1
                self.sec = 0
                self.min = 0
            elif self.sec == 59 and self.min == 59 and self.hr == 23:
                self.min = 0
                self.sec= 0
                self.hr = 0
            print('{:02d}:{:02d}:{:02d}'.format(hr,min, sec),end='\r')
            time.sleep(1)    
    
    
    
    