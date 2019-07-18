#!/data/data/com.termux/files/usr/bin/python

import os
import sys
from time import sleep
from core.rsfcore import *

print("/$$$$$$$                        /$$                                             /$$           /$$   /$$		")
print("| $$__  $$                      | $$                                            | $$          |__/  | $$		")
print("| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$	")
print("| $$$$$$$/ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$| $$ /$$__  $$| $$|_  $$_/	")
print("| $$__  $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$| $$  \__/|  $$$$$$ | $$  \ $$| $$| $$  \ $$| $$  | $$		")
print("| $$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$       \____  $$| $$  | $$| $$| $$  | $$| $$  | $$ /$$	")
print("| $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$| $$       /$$$$$$$/| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/	")
print("|__/  |__/ \______/  \______/    \___/   \_______/|__/      |_______/ | $$____/ |__/ \______/ |__/   \___/	")
print("                                                                      | $$					")
print("                                                                      | $$                                       ")
print("                                                                      |__/                                  	")
print("                     /$$                                                                                    	")
print("                    | $$                                                                                    	")
print("                   /$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$   /$$ /$$   /$$				")
print("                  |_  $$_/   /$$__  $$ /$$__  $$| $$_  $$_  $$| $$  | $$|  $$ /$$/				")
print("                    | $$    | $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$  | $$ \  $$$$/				")
print("                    | $$ /$$| $$_____/| $$      | $$ | $$ | $$| $$  | $$  >$$  $$                           	")
print("                    |  $$$$/|  $$$$$$$| $$      | $$ | $$ | $$|  $$$$$$/ /$$/\  $$                          	")
print("                     \___/   \_______/|__/      |__/ |__/ |__/ \______/ |__/  \__/                          	")

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

