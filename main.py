#################################################
#	Sensor Reading Program and sending payload	#
#	Created by Group_3					        #
#	Not needed to import any other sensors      #
#   Version 1.0                         		#
#################################################

from network import LoRa
import socket
import time
import binascii
import pycom
 
from lib.LTR329ALS01 import LTR329ALS01
from lib.SI7006A20 import SI7006A20
from lib.L76GNSS import L76GNSS

pycom.heartbeat(False)
pycom.rgbled(0x000000)
 
# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, adr=True)
 
APP_EUI = '70 B3 D5 7E D0 01 4F 57'
APP_KEY = '42 D1 58 28 12 9D 95 4F 08 E9 DE 97 0B 1E DB 9D'
# join a network using OTAA (Over the Air Activation)
app_eui = binascii.unhexlify(APP_EUI.replace(' ',''))
app_key= binascii.unhexlify(APP_KEY.replace(' ',''))
 
# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
 
# wait until the module has joined the network
count = 0
while not lora.has_joined():
    pycom.rgbled(0xff0000)
    time.sleep(2.5)
    pycom.rgbled(0x000000)
    print("Not yet joined count is:" ,  count)
    count = count + 1
 
# create a LoRa socket
pycom.rgbled(0x0000ff)
time.sleep(0.1)
pycom.rgbled(0x000000)
time.sleep(0.1)
pycom.rgbled(0x0000ff)
time.sleep(0.1)
pycom.rgbled(0x000000)
 
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
 
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
 
# make the socket non-blocking
s.setblocking(False)
 
# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)
 
# init the libraries
lib_1 = LTR329ALS01()
lib_2 = SI7006A20()
lib_3 = L76GNSS()
 
while True:
    # Read data from the libraries and place into string
    payload = "%.2f %.2f %.2f %.2f %.2f" % (lib_1.temperature(), lib_1.light()[0], lib_2.humidity(), lib_3.coordinates())
    
    #printing data to terminal
    print("Sending %s" % payload)
    
    # send the data over LPWAN network
    s.send(payload)

    #blink LED on green once data sent
    pycom.rgbled(0x00ff00)
    time.sleep(0.1)
    pycom.rgbled(0x000000)

    #DELAY 20sec
    time.sleep(100)
