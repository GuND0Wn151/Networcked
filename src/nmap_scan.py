import os
from subprocess import PIPE, run
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
