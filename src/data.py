def Owasp_top():
	
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----Owasp-top-10-----")
	print(green+"\nThis option tell about the 10 most common application vulnerabilities.\n\ncommand:\n\netw --info or netw --i\nthen it will provide you list of those vulneabilites\n\nselect any one of them to know about them."+nc)

def password():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----cve_detalis-----")
	print(green+"\nThis option is used to crack passwords\ncommand:\nnetw --pass"+nc)

def cve_detalis():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----cve_detalis-----")
	print(green+"\nThis option gives you cve details\nCVE, short for Common Vulnerabilities and Exposures, \nis a list of publicly disclosed computer security flaws. \nWhen someone refers to a CVE, they mean a security flaw that's been assigned a CVE ID number.\nSecurity advisories issued by vendors and researchers almost always mention at least one CVE ID. \nCVEs help IT professionals coordinate their efforts to prioritize and address these vulnerabilities \nto make computer systems more secure.\ncommand:\nnetw --cve\nexample\nnetw --cve CVE-2019-19781" +nc )


def apache_server():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----apache_server-----")
	print(green + "\nThis option is used to start an Apache server.\ncommand:\nnetw --server"+nc)


def directory_finder():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----directory_finder----")
	print(green+"\nThis option is used to find the directory\ncommand:\nnetw --d"+nc)


def nmap_scan():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----nmap_scan-----")
	print(green+"\nThis option is used to check the number of open ports in an IP address\ncommand:\nnetw --scan or netw --s (ip address)"+nc)

def payload_venom():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----payload_venom-----")
	print(green+"\nHere we give the payload number which tells in which platform or language it is going to be used.\nAfter the command is executed it prints the directory where the payload is created.\nThe -p flag: Specifies what payload to generate\nThe -f flag: Specifies the format of the payload\ncommand:\nnetw --payload (number)"+nc)


def hash_identify():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----hash_identify-----")
	print(green+"\nAn input will be give as hash.\nIt will tell which hash algorithm is used.\ncommand:\nnetw --hash"+nc)


def searchsploit():
	nc='\033[0m'
	green='\033[0;32m'
	print(green+"\n-----searchsploit-----")
	print(green+"\nIt will give scripts/vulnerabilites of the parameter or technologies given in command.\nWe can also download the script.\ncommand:\nnetw --search"+nc)
