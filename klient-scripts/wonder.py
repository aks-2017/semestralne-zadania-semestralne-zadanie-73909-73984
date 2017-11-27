import time
import os
print "nastavujem BW na rozhrani na 1024"
os.system("wondershaper enp5s0f1 1024 1024")
time.sleep(30)
print "nastavujem BW na rozhrani na 2048"
os.system("wondershaper enp5s0f1 2048 2048")
time.sleep(30)
print "nastavujem BW na rozhrani na 3072"
os.system("wondershaper enp5s0f1 3072 3072")
time.sleep(30)
print "nastavujem BW na rozhrani na 1024"
os.system("wondershaper enp5s0f1 1024 1024")
time.sleep(30)
print "nastavujem BW na rozhrani na default hodnotu"
os.system("wondershaper clear enp5s0f1")

