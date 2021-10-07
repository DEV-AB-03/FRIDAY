import time
import datetime
strtime=datetime.datetime.now().strftime("%H:%M:%S")
t = time.strptime(strtime, "%H:%M:%S")
timevalue_12hour = time.strftime( "%I:%M %p", t )
print(timevalue_12hour)