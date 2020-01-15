import os
def func():
 try:
  while True:
   d=os.stat("./text/dbm.txt").st_size == 0
   if d==False:
    global avg
    total=0
    count=0
    f1=open('./text/dbm.txt','r')
    for i in f1:
      i=i.strip()
      i=i.strip('-')
      if i == '':
       i='0'
       count=count-1
       print(i)
      total=total+int(i)
      count=count+1       
    avg=str((total/count))
    f2=open('./text/mail.txt','w')
    f2.write(avg)
    f2.close()
    print(avg)
    os.system('cp /dev/null ./text/dbm.txt')       
    f1.close()
 except ZeroDivisionError:
  pass


func()
