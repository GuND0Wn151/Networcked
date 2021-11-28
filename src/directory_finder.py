import os
import time
import requests

RED='\033[0;31m'
NC='\033[0m'
green='\033[0;32m'
cyan='\033[0;36m'
orange='\033[0;33m'
purple='\033[0;35m'

def Direc_find(a):
	a=a.split()
	if(a[0]=="netw"):
		if a[1]=="--direc":
			t=open(a[3],"r")
			for i in t:	
				x=repr(i).replace(r'\n',"")
				req=requests.get(a[2]+"/"+x)
				if req.status_code<300:
					print(green+req.status_code+NC+" "+a[2]+"/"+x)
				else:
					print(RED+req.status_code+NC+" "+a[2]+"/"+x)

