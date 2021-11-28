import os
import time
import requests


def Direc_find(a):
	RED='\033[0;31m'
	NC='\033[0m'
	green='\033[0;32m'
	cyan='\033[0;36m'
	orange='\033[0;33m'
	purple='\033[0;35m'

	a=a.split()
	if(a[0]=="netw"):
		if a[1]=="--direc":

			print()
			os.system("echo '\033[0;31m [Starting] \033[0m Loading The Modules...'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Opeing the file...'")
			time.sleep(1)
			print()
			os.system("echo '\033[0;31m [Retrieving  the Data] \033[0m  Almost there.....'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;32m [Got The Info !!] \033'")
			print()
			t=open(a[3],"r")
			for i in t:	
				x=repr(i).replace(r'\n',"")
				req=requests.get(a[2]+"/"+x)
				if req.status_code<300:
					print(green+req.status_code+NC+" "+a[2]+"/"+x)
				else:
					print(RED+req.status_code+NC+" "+a[2]+"/"+x)

