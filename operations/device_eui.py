import binascii
import network
print("Device EUI: "+str(binascii.hexlify(network.LoRa().mac())))
