import os
#os.system("airmon-ng check kill")
#os.system("airmon-ng check kill") #To prevent interference from changing channels and putting the interface back in Promiscuous mode.
print("PUTTING WIRELESS ADAPTER INTO MONITOR MODE")
os.system("airmon-ng start wlan1")
os.system("ifconfig")
print("\n\n")
print("TO PUT ADAPTER BACK TO PROMISCOUS MODE->TYPE exit")
name=input()
while name!='exit':
	name=input('its exit,type again:')
	
os.system("airmon-ng stop wlan1mon")

