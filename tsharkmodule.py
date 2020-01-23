import os

os.system('cp /dev/null ./text/logtest.txt')
os.system('cp /dev/null ./text/deauthlog.txt')
os.system('sudo tshark -V -i wlan1mon -n -Y "((wlan.fc.type == 0)&&(wlan.fc.type_subtype == 0x0c))" |tee -a ./text/log.txt ./text/deauthlog.txt ./text/logtest.txt > /dev/null')

