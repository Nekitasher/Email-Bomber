import smtplib # send emails in python
import sys # exit and stuff
from threading import Thread
#import optparse

your_email = "yourEmail" # email that sends
your_password = "yourPassword" # password to that email

print()
their_email = input("email    : ")
message = input("message  : ")

received = 0

def send():
	global received

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587) # connect to server
		server.starttls() 
		server.login(your_email, password) # person sending
		server.sendmail(your_email, their_email , message) # send the message
		server.quit() # close

		received += 1
		print(str(received) + " sent")
		
		
	except smtplib.SMTPRecipientsRefused:
		print("\nYou may have entered an invalid email")

	except KeyboardInterrupt:
		print("\n[-] quiting")
		sys.exit()


def endless():
	while True:
		send()


def amount():
	amounts = int(input("amount	 : "))
	for x in range(1, amounts + 1):
		send()
	
	print(str(x) + " Sent")
	print("\nDone!")


ea = int(input("\n[1]: endless\n[2]: amount\n\n>> "))

if ea == 1:
	endless()

if ea == 2:
	amount()

else:
	print("thats not an option bud")
