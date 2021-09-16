from datetime import datetime

'''
Version: 1.0
^______^
'''

class TimeNow:
    def __init__(self):
        self.dt = datetime.now()

    def check_time(self):
        self.dt_time = int(self.dt.strftime("%H%M"))
        return self.dt_time

    def check_date(self):
        self.dt_date = self.dt.strftime("%d %m %Y")
        return self.dt_date


if __name__ == "__main__":
    while True:
        c = TimeNow()
        print(c.check_time())
