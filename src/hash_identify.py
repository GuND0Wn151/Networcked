import os
from subprocess import PIPE, run
import time
def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

def hash_iden(a):
	RED='\033[0;31m'
	NC='\033[0m'
	green='\033[0;32m'
	cyan='\033[0;36m'
	orange='\033[0;33m'
	purple='\033[0;35m'
	a=a.split()
	if "--hash" in a:
		print()
		os.system("echo '\033[0;31m [Starting] \033[0m Loading The Modules...'")
		print()
		time.sleep(1)
		os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Decoding...'")
		time.sleep(1)
		print()
		os.system("echo '\033[0;31m [Retrieving  the Data] \033[0m  Almost there.....'")
		print()
		time.sleep(1)
		os.system("echo '\033[0;32m [Got The Info !!] \033'")
		print()
		print("The Possible Hashes Can be:- ")
		print("\n---------------------------------------\n")
		#print(a[2])
		os.system("haiti "+a[2])
		print("\n---------------------------------------\n")
		#print(x)


# a=input("Enter Your Command: ").split()
# hash_identify(a)

#https://patorjk.com/software/taag/#p=display&f=3D-ASCII&t=Networcked
