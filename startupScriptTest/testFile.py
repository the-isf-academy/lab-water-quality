
import io
import sys
import fcntl
import time
import copy
import string
from datetime import datetime
import csv
       
def main():
    num = 0
    for i in range(10):
        with open('/home/pi/cs10_unit01_project/startupScriptTest/data.csv',mode='a') as file:
            file_writer = csv.writer(file,delimiter=',')
            file_writer.writerow(['date/time',"data"])
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_writer.writerow([date_time,num])
            num += 1
                
        
          

if __name__ == '__main__':
    main()
