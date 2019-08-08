#!/data/data/com.termux/files/usr/bin/python

import os
import sys
from time import sleep
from core.rsfcore import *

sleep(1)
print("RoutersploitTermux by Cose")
print("")
sleep(1)

print("Welcome to routersploit installer!")
sleep(2)
print("You will be redirected to the installer...")
sleep(2)
print("")

print("Are you sure want to install routersploit? ( y or n )")
permission = input(">>> ")

if permission == 'y':
	print("Now installing routersploit...")
	sleep(2)
	runscript()

elif permission == 'n':
	print("Aborting download...")
	sleep(1)

else:
	print("Dont know lang... Exiting...")
	sleep(1)

