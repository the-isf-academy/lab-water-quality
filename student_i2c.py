import io
import sys
import fcntl
import time
import copy
import string
from AtlasI2C import (
	 AtlasI2C
)
from view import View
from datetime import datetime
from pytz import timezone
import csv

hong_kong = timezone('Asia/Hong_Kong')
       
def main():

    view = View()
    device_list = view.get_devices()
    device = device_list[0]
    print(sys.argv)
    print(len(sys.argv)) 
    
    if len(sys.argv) >= 2:
        delaytime = float(sys.argv[1])
    if len(sys.argv) >= 3:
        num_poll = int(sys.argv[2])
    if len(sys.argv) == 1:
        num_poll = 10
        delaytime=device.long_timeout
    
    if delaytime < device.long_timeout:
        print("Polling time is shorter than timeout, setting polling time to %0.2f" % device.long_timeout)
        delaytime = device.long_timeout

    with open('data.csv',mode='a+') as file:
        file_writer = csv.writer(file,delimiter=',')
        file_writer.writerow(['date/time',device.get_device_datatype()])
        for i in range (num_poll):
            device.write("R")
            time.sleep(delaytime)
            print(device.read())
            plain_data = device.get_plain_data() 
            date_time = datetime.now(hong_kong).strftime("%Y-%m-%d %H:%M:%S")
            file_writer.writerow([date_time,plain_data])
        
          

if __name__ == '__main__':
    main()
