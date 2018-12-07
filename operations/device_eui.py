#####################################################
#	Commands to get Devide EUI                      #
#	Created by Group_3					            #
#####################################################
import binascii
import network
print("Device EUI: "+str(binascii.hexlify(network.LoRa().mac())))
