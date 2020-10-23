import io
import sys
import fcntl
import time
import copy
import string
from AtlasI2C import (
	 AtlasI2C
)

class View:

    def print_help_text(self):
        print('''
    >> Atlas Scientific I2C sample code
    >> Any commands entered are passed to the default target device via I2C except:
    - Help
        brings up this menu
    - Poll[,x.xx]
        command continuously polls all devices
        the optional argument [,x.xx] lets you set a polling time
        where x.xx is greater than the minimum %0.2f second timeout.
        by default it will poll every %0.2f seconds
    >> Pressing ctrl-c will stop the polling
        ''' % (AtlasI2C.LONG_TIMEOUT, AtlasI2C.LONG_TIMEOUT))

    def print_devices(self,device_list, device):
        for i in device_list:
            if(i == device):
                print("--> " + i.get_device_info())
            else:
                print(" - " + i.get_device_info())
        #print("")

    def print_device_info(self,device):
        print("Current Device: " + device.get_device_info())
    
    def get_devices(self,):
        device = AtlasI2C()
        device_address_list = device.list_i2c_devices()
        device_list = []
        
        for i in device_address_list:
            device.set_i2c_address(i)
            response = device.query("I")
            moduletype = response.split(",")[1] 
            response = device.query("name,?").split(",")[1]
            device_list.append(AtlasI2C(address = i, moduletype = moduletype, name = response))
        return device_list 


