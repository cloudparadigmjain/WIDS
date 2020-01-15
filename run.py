import os 
from subprocess import call
os.system('cp /dev/null ./text/details.txt')
list1=['a','b','c']
list1[0]=raw_input("Enter reciever email")
list1[1]=raw_input("Enter sender email")
list1[2]=raw_input("Enter sender password") 
for i in list1:
	f2=open('./text/details.txt','a')
	f2.write(i +'\n')
	f2.close()
call(['gnome-terminal','--geometry','80x18+0+0','-e',"python3 adaptormon.py"])
call(['gnome-terminal','--geometry','60x18+1000-700','-e',"python3 tsharkmodule.py"])
call(['gnome-terminal','--geometry','40x15+0+415','-e',"python3 val.py"])
call(['gnome-terminal','--geometry','45x15+1000+415','-e',"python3 signalstrength.py"])
call(['gnome-terminal','--geometry','50x15-200+415','-e',"python3 fchkandsendmail.py"])



