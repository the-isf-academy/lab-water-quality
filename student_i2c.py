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


       
def main():

    view = View()

    device_list = view.get_devices()
    device = device_list[0]

    view.print_help_text()
    view.print_devices(device_list,device)

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
                while True:
                    print("-------press ctrl-c to stop the polling")
                    for dev in device_list:
                        dev.write("R")
                    time.sleep(delaytime)
                    for dev in device_list:
                        print(dev.read())
                
            except KeyboardInterrupt:       # catches the ctrl-c command, which breaks the loop above
                print("Continuous polling stopped")
                print_devices(device_list, device)
                
        
          

if __name__ == '__main__':
    main()
