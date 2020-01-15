import test
import smtplib
import os
list1=['1','2','3']
count=0
f1=open('./text/details.txt','r')
for i in f1:
	if i=='\n':
		continue		
	else:
		i=i.strip('\n')		
		list1[count]=i
		count=count+1
f1.close()	

print(list1)
while True:
#print('hye')
	d=os.stat("./text/deauthlog.txt").st_size == 0
	if d==False:
		e=os.stat("./text/mail.txt").st_size == 0
		if e==False:
			f1=open('./text/mail.txt','r')
			for i in f1:
				avg=i                 	
			print("Mail Sent!!!!!!!!")
			#Create SMTP session
			mail_obj=smtplib.SMTP('smtp.gmail.com',587)
			#Start TLS for encrypting your messages
			mail_obj.starttls()
			#Authenticate Sender with Login credentials such as EmailId and Password
			mail_obj.login(list1[1],list1[2])
			#Message to be sent
			message='Deauth DDOS attack detected,average signal of attacker is - '
			#Send the EMAIL
			mail_obj.sendmail(list1[1],list1[0],message + str(avg) + str('dbm'))
			#Terminating the session
			mail_obj.quit()
			# Download the helper library from https://www.twilio.com/docs/python/install
			#! /usr/bin/python3
			from twilio.rest import Client


			# Your Account Sid and Auth Token from twilio.com/console
			# DANGER! This is insecure. See http://twil.io/secure
			account_sid = '<Your Account_SID>'
			auth_token = '<Your Auth Token>'
			client = Client(account_sid, auth_token)

			numbers_to_message = ['+919826159719','+918989438840','+919901914554']
			for number in numbers_to_message:
    				client.messages.create(
        				body = message +str(avg)+str('dbm'),
        				from_ = '+15702250256',
        				to = number
    				)

			#print(message.sid)
			os.system('cp /dev/null ./text/deauthlog.txt')

