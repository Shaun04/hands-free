from checktime import * 
from maindbscript import *

'''
Version: 1.0
Date: 09-08-2021
:)
'''

class SchedulingLogic:
    def __init__(self):
        self.ct = TimeNow()
        self.maindb = TaskCreater()
    
    def filtering_data(self): #this function checks if the schedule time of event isnt passed so it can run properly
        num_items = self.maindb.read_data(self.ct.check_date())
        if len(num_items) == 0:
            print("No data")
        else:        
            num_items = [item for item in num_items if item[1] >= self.ct.check_time()]
            num_items = sorted(num_items)         #Sorting the data now
            return num_items


if __name__ == "__main__":
    c = SchedulingLogic()
    c.filtering_data()









