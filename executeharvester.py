'''
Python program to call and run The Harvester programs Kali linux
Program by HIT ISA students: John Chakauya, Gerald Gobvu, Rutendo Bingura, Blessing Njekezana and Neville Mahove
'''

import os, sys

print("** WELCOME TO THE HARVESTER Powered by HIT ISA Students **")
print("Enter exit to exit the app...")
help = raw_input("Do you want to view The Harvester help? yes or no \n")
if help == "yes":
	os.system("theharvester")
elif help == "exit":
	sys.exit()

domain = raw_input("Enter the Domain: ")
if domain == "exit":
	sys.exit()
data_source = raw_input("Enter the Data Source: ")
if data_source == "exit":
	sys.exit()

os.system("theharvester -d " + domain + " -b " + data_source)
