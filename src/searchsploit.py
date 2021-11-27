import os
from subprocess import PIPE, run
def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

def searchsploit(a):

	if "--search" in a:
		os.system("searchsploit "+" ".join(a[2:]))
		print("\nThe Exploits are available at /usr/share/exploitdb/exploits/ +  the Path provided\n")

