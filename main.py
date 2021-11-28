from src.logo import logo_print
from src.data import *
from src.apache_server import start_server
from src.directory_finder import Direc_find
from src.nmap_scan import *
from src.owasp_top import get_top_10
from src.searchsploit import searchsploit_info
from src.hash_identify import hash_iden
from src.cve_details import CVE_details
from src.payload_venom import payloads_msf
from src.directory_finder import Direc_find
RED='\033[0;31m'
nc='\033[0m'
green='\033[0;32m'
cyan='\033[0;36m'
orange='\033[0;33m'
purple='\033[0;35m'
import os
os.system("clear")
logo_print()

print(RED+"\t\n-----List of Services-------"+nc)
print(cyan+"\t\n1. Python/Apache Server")
print("\t\n2. Port Scanning Using Nmap ")
print("\t\n3. Documentations and Information")
print("\t\n4. Scripts and Payloads")
print("\t\n5. Hashes Identifer")
print("\t\n6. Directory and CVE Details"+nc)
print(RED+"\t\n------------------------------"+nc+"\n")

a=input("Choose The Category:- ")
if a=="1":
	apache_server()
	directory_finder()
	print()
	data=input("Enter the Command:- ")

	start_server(data)

	Direc_find(data)
	

elif a=="2":
	nmap_scan()
	print()
	data=input("Enter the Command:- ")
	if "--extra" in data:
		ip=input("Enter the IP:- ")
		nmap_scan_extra(data,ip)
	else:
		nmap_scan()

elif a=="3":
	Owasp_top()
	print()
	data=input("Enter the Command:- ")
	get_top_10(data)


elif a=="4":
	payload_venom()
	searchsploit()
	print()
	data=input("Enter the Command:- ")
	payloads_msf(data)
	searchsploit_info(data)

elif a=="5":
	hash_identify()
	print()
	data=input("Enter the Command:- ")
	hash_iden(data)

elif a=="6":
	cve_detalis()
	directory_finder()
	print()
	data=input("Enter the Command:- ")
	CVE_details(data)
	Direc_find(data)
