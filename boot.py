#####################################################
#	Boot section to define communication and        #
#   select class which will run once LoPy powered   #
#	Created by Group_3					            #
#####################################################
from machine import UART
import machine
import os

uart = UART(0, baudrate=115200)
os.dupterm(uart)

#machine.main('main.py')
