import os
from subprocess import PIPE, run

def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

def hash_identify(a):

	if "--hash" in a:
		print("The Possible Hashes Can be:- ")
		print("\n---------------------------------------\n")
		os.system("haiti "+a[2])
		print("\n---------------------------------------\n")
		#print(x)


# a=input("Enter Your Command: ").split()
# hash_identify(a)

#https://patorjk.com/software/taag/#p=display&f=3D-ASCII&t=Networcked
