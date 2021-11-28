from bs4 import BeautifulSoup
import os
import time
import requests
RED='\033[0;31m'
NC='\033[0m'
green='\033[0;32m'
cyan='\033[0;36m'
orange='\033[0;33m'
purple='\033[0;35m'

def CVE_details(n):
	c=n.split()
	if(c[0]=='netw'):
		if(c[1]=='--cve'):
			link="https://www.cvedetails.com/cve/"
			op=link+c[2]
			req = requests.get(op)
		  
			soup=BeautifulSoup(req.text,'lxml')
			table=soup.find('table', id="cvssscorestable")
			r=table.find_all('tr') 
			print()
			os.system("echo '\033[0;31m [Starting] \033[0m Loading The Modules...'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Requests...'")
			time.sleep(1)
			print()
			os.system("echo '\033[0;31m [Retrieving  the Data] \033[0m  Copying Pages.....'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;32m [Got The Info !!] \033'")
			print()
			time.sleep(1)
			dic={}
			for i in r:
				h=i.find_all('th')
				table_data = i.find_all('td')
				he=[j.text for j in h]
				data = [j.text for j in table_data]
				for i in range(len(he)):
					dic[he[i]]=data[i]
			for i in dic.keys():
				t=dic[i].replace('\n',"  ")
				t="".join(t)
				dic[i]=t
			for k, v in dic.items():
			   label=v
			   print(f"{orange}{k}{NC} : {green}{label} {NC} ")
			   #print("\n")
		
		
# a=input('Enter Command:')
# CVE_details(a)          
