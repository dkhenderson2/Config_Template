#!/usr/bin/python3

from EmailMsg import Send_Email
from prompter import yesno
from IPy import IP
from netaddr import *
import pprint
import sys
import time

TS =  time.sleep
orig_stdout = sys.stdout

while True:
        try:
                MOD = int(input("Choose a Model\n 1. 55XX-X\n 2. 5506-X\n 3. 5506-X(SW)\n 4. 55XX\n 5. 5505\n Please enter your selection Number: "))
                if MOD <= 5 and MOD != 0:
                        False
                else:
                        true
                break
        except:
                print(".")
                TS(0.5)
                print(".")
                TS(0.5)
                print("Come On!  That wasn't even an option.  Try again...")
                print(".")
                TS(0.5)
                print(".")
                TS(0.5)
TS(0.25)
print(".")
TS(0.25)
print(".")
TS(0.25)
print(".")
if MOD == "1":
        print("Setting model to 55XX-X")
        MOD = "55XX-X"
elif MOD == "2":
        print("Setting model to 5506-X")
        MOD = "5506-X"
elif MOD == "3":
        print("Setting model to 5506-X(SW)")
        MOD = "5506-X(SW)"
elif MOD == "4":
        print("Setting model to 55XX")
        MOD = "55XX"
else:
        print("Setting model to 5505")
        MOD = "5505"


while True:
        try:
                DIV = int(input("Choose a Division\n 1. YOH\n 2. SOC\n 3. ECM\n 4. M&H\n 5. DZMG\n Please enter your selection Number: "))
                if DIV <= 5 and DIV != 0:
                        False
                else:
                        true
                break
        except:
                print(".")
                TS(0.5)
                print(".")
                TS(0.5)
                print("Come On!  That wasn't even an option.  Try again...")
                print(".")
                TS(0.5)
                print(".")
                TS(0.5)
TS(0.25)
print(".")
TS(0.25)
print(".")
TS(0.25)
print(".")
if DIV == "1":
        print("Setting Division to YOH")
        DIV = "YOH"
elif DIV == "2":
        print("Setting Division to SOC")
        DIV = "SOC"
elif DIV == "3":
        print("Setting Division to ECM")
        DIV = "ECM"
elif DIV == "4":
        print("Setting Division to M&H")
        DIV = "MH"
else:
        print("Setting Division to DZMG")
        DIV = "DZMG"

CITY = input("Please enter The City: ")
print ("Setting City to ", CITY)

while True:
        try:
                CRYPT = int(input("Please enter The cryptomap Number: "))
                break
        except:
                print("Oops!  That was no valid number.  Try again...")

print ("Setting Cryptomap to ", CRYPT)

ARPT = input("Please enter The Airport Code: ")
print ("Setting Airport Code to ", ARPT)

HA = yesno('Will this be a HA Pair?', default='no')
print ("Setting HA Pair in config")

DHCP = yesno('Enable DHCP for the DATA VLAN?', default='no')
print ("Setting DATA DHCP config")

VOICE = yesno('Enable DHCP for the VOICE VLAN?', default='no')
print ("Setting Voice interface in config")

while True:
	try:
		WAN = input("Enter the WAN IP: ")
		WMASK = input("Enter the WAN Mask using CIDR notation(/X): ")
		IP(WAN)
		WANIP = IPNetwork(WAN+WMASK)
		WANMASK = WANIP.netmask
		if IP(WAN).iptype() == 'PRIVATE':
			true
		else:
			False
		break
	except:
		print("You have entered an invaled IP address.  Try again...")

print ("Setting WAN IP to ", WAN, WANMASK)

while True:
        try:
                LAN = input("Enter the LAN IP(Should be the actual outside interface IP): ")
                LMASK = input("Enter the LAN Mask using CIDR notation(/X): ")
                IP(LAN)
                LANIP = IPNetwork(LAN+LMASK)
                LANMASK = LANIP.netmask
                break
        except:
                print("You have entered an invaled IP address.  Try again...")

print ("Setting LAN IP to ", LAN, LANMASK)

#NAME = name.upper()


with open('output3.txt', 'w') as f:
    sys.stdout = f
    print ("test")

sys.stdout = orig_stdout
f.close()

#Send_Email(DIV,CITY,CRYPT)

