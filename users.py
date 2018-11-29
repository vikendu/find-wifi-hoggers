import subprocess
import ipaddress
from subprocess import Popen, PIPE
import re

network = ipaddress.ip_network('192.168.1.0/24')
for i in network.hosts():
	i = str(i)
	toping = Popen(['ping', '-c','3',i], stdout = PIPE)
	output = toping.communicate()[0]
	hostalive = toping.returncode
	if hostalive == 0:
		print(i, 'Available')
		pid = Popen(["arp", "-n", i], stdout = PIPE)
		s = pid.communicate()[0].decode("utf-8")
		mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
		if mac is None:
			continue

		else:
			print(mac.groups()[0])
	
	elif(i == '192.168.1.20'):
		break

	else:
		print(i, 'Unavailable')

	
