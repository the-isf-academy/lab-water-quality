from AtlasI2C import AtlasI2C
from datetime import datetime
from time import sleep
from pytz import timezone
import csv

hong_kong = timezone('Asia/Hong_Kong')


def interface():
    '''A command line itnerface for an AtlasScientific Water Sensor'''

    controller = AtlasI2C()
    device = AtlasI2C(address=controller.list_i2c_devices()[0])

    with open('data_tank.csv',mode='a+') as file:
        file_writer = csv.writer(file,delimiter=',')
        file_writer.writerow(['date'])

        date = datetime.now(hong_kong).strftime("%d-%m-%Y")
        file_writer.writerow([date])

        device.write("R")
        sleep(device.long_timeout)
        print(device.read())


if __name__ == '__main__':
    interface()