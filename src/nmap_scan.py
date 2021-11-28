import os
from subprocess import PIPE, run
import time
def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

def print_ports(data):
	t=0
	for i in x:
		if "PORT" in i:
			t=1
		if t==1:
			print(i)
		if "Nmap done" in i:
			break

def nmap_scan_extra(a,ip):
	if "--extra" in a:
		RED='\033[0;31m'
		NC='\033[0m'
		green='\033[0;32m'
		cyan='\033[0;36m'
		orange='\033[0;33m'
		purple='\033[0;35m'
		print()
		os.system("echo '\033[0;31m [Starting] \033[0m Loading The Modules...'")
		print()
		time.sleep(1)
		os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Scanning...'")
		time.sleep(1)
		print()
		os.system("echo '\033[0;31m [Retrieving  the Data] \033[0m  Almost there.....'")
		print()
		time.sleep(1)
		os.system("echo '\033[0;32m [Got The Info !!] \033'")
		print()
		params=""
		for i in a:
			if i[:2]=="--":
				params+=i+" "
			try:
				x=command("nmap "+params+ip)
				x=str(x).split(r'\n')
				return(x)
			
			except:
				print("Please enter a valid IP or Valid Paramaters!")

def nmap_scan(a):
	
	if a[0]=="netw":
		try:
			if "--scan" or "--s" in a:
				RED='\033[0;31m'
				NC='\033[0m'
				green='\033[0;32m'
				cyan='\033[0;36m'
				orange='\033[0;33m'
				purple='\033[0;35m'
				print()
				os.system("echo '\033[0;31m [Starting] \033[0m Loading The Modules...'")
				print()
				time.sleep(1)
				os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Scanning...'")
				time.sleep(1)
				print()
				os.system("echo '\033[0;31m [Retrieving  the Data] \033[0m  Almost there.....'")
				print()
				time.sleep(1)
				os.system("echo '\033[0;32m [Got The Info !!] \033'")
				print()
				ip=""
				for i in a:
					if i.count('.')>2:
						ip=i
						a.remove(i)
				if ip!="":
					data=nmap_scan(a,ip)
					print_ports(data)
				
				if "Host seems down" in data:
					print("The Host is down")
				print_ports(data)
		except:
			print("Incorrect Command Please Enter Proper Parameters")
