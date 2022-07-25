import subprocess
import platform
import netifaces as ni
import shutil
from colors import blue

def ping_host(host):
	print("I am using " + platform.system() + " Platform")
	ip = ni.ifaddresses('enp0s8')[ni.AF_INET][0]['addr']
	print("My IP address" + blue(" is ") + ip)
	response = subprocess.call(['ping', '-c', '1', host], stdout = subprocess.DEVNULL)
	if response == 0:
		return blue("and ") + host + blue(" is") + " reachable"
	else:
		return "and " + host + " is not reachable"
print(ping_host("www.neti.ee"))
