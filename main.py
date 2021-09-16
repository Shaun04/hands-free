from scheduler import *
from notification_module import *
from checktime import *
from maindbscript import *
import time as t
import webbrowser
import sys

'''
Version: 1.0
^______^
'''

sys.setrecursionlimit(1440)

class MainRun:
    def __init__(self):
        self.main_logic = SchedulingLogic()
        self.notification_module = NotifyMe
        self.ct = TimeNow()
        
    def run_program(self):
        try:
            date, time, title, data, link = map(list, zip(*self.main_logic.filtering_data()))
            time_var, title_var, data_var, link_var = time.pop(0), title.pop(0), data.pop(0), link.pop(0)
            print("Next alarm is at: " + str(time_var))
            while True:
                self.time_check = TimeNow()
                if time_var - 1 == self.time_check.check_time():
                    print("Sleeping for 20 secs")
                    t.sleep(20)
                elif time_var == self.time_check.check_time():
                    self.notification_module.first(title_var, data_var)
                    t.sleep(10)
                    webbrowser.open(link_var)
                    t.sleep(50)
                    break
                
                else: 
                    print("Sleeping for a min. Time now:  " + str(self.time_check.check_time()))
                    t.sleep(60)
            c = MainRun()    
            c.run_program()

        except ValueError:
            print("No values, Waiting")
            t.sleep(60)
            c = MainRun()
            c.run_program()
        except TypeError:
            print("Type Error Sleeping.")
            t.sleep(120)
            c = MainRun()
            c.run_program() 
        except Exception as exception:
            time_and_date = str(self.ct.dt)
            data_to_file = "Main.py \n {} Exception: {} : {}".format(time_and_date[0:19], type(exception).__name__, exception)
            print("Error quiting")
            with open("errors.txt", "a") as wf:
                wf.write(data_to_file)
            self.notification_module.first("Crashed", "Check error.txt for more information")
            
            

NotifyMe.first("Hello", "Automation is turned on and is ready")
c = MainRun()    
c.run_program()
