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
import csv
       
def main():

    view = View()
    device_list = view.get_devices()
    device = device_list[0]
   
    view.print_device_info(device)
    view.print_help_text()

    real_raw_input = vars(__builtins__).get('raw_input', input)
    
    while True:
    
        user_cmd = real_raw_input(">> Enter command: ")
        
        # show all the available devices
        if user_cmd.upper().strip().startswith("LIST"):
            view.print_devices(device_list, device)
            
        # print the help text 
        elif user_cmd.upper().startswith("HELP"):
            view.print_help_text()
            
        # continuous polling command automatically polls the board
        elif user_cmd.upper().strip().startswith("POLL"):
            cmd_list = user_cmd.split(',')
            if len(cmd_list) > 1:
                delaytime = float(cmd_list[1])
            else:
                delaytime = device.long_timeout

            # check for polling time being too short, change it to the minimum timeout if too short
            if delaytime < device.long_timeout:
                print("Polling time is shorter than timeout, setting polling time to %0.2f" % device.long_timeout)
                delaytime = device.long_timeout
            try:
                with open('data.csv',mode='w') as file:
                    file_writer = csv.writer(file,delimiter=',') 
                    while True:
                        print("-------press ctrl-c to stop the polling")
                    
                        device.write("R")
                        time.sleep(delaytime)
                        print(device.read())
                        plain_data = device.get_plain_data() 
                        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        file_writer.writerow([date_time,plain_data])
            except KeyboardInterrupt:       # catches the ctrl-c command, which breaks the loop above
                print("Continuous polling stopped")
                
        
          

if __name__ == '__main__':
    main()
