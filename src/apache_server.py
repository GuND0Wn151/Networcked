import os
import time
import webbrowser
from subprocess import PIPE, run

def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

# a=input(f'{green}Enter Command:{NC}').split()


def start_server(a):
	a=a.split()
	if(a[0]=="netw"):
		if "--server" in a:
			t="sudo service apache2 start -D "+a[2]
			x=command(t)
			webbrowser.open("http://localhost/")
			
		if '--file' in a:
			command('sudo rm /var/www/html/index.nginx-debian.html')
			print()
			os.system("echo '\033[0;31m [Starting] \033[0m Loading The Server...'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;31m [Initializing] \033[0m Starting The Processes....'")
			time.sleep(1)
			print()
			os.system("echo '\033[0;31m [Loading The Host] \033[0m  Copying Pages.....'")
			print()
			time.sleep(1)
			os.system("echo '\033[0;32m [All Set !!] \033[0m Server Deployed At http://localhost...'")
			print()
			time.sleep(1)
			t='sudo cp '+a[2]+' /var/www/html/src/cindex.html'
			command('mkdir /var/www/html/src')
			x=command(t)
			#print(t)
			webbrowser.open("http://localhost/src/index.html")
