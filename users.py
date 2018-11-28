import subprocess
import ipaddress
from subprocess import Popen, PIPE

network = ipaddress.ip_network('192.168.1.0/24')
for i in network.hosts():
	i = str(i)
	toping = Popen(['ping', '-c','3',i], stdout = PIPE)
	output = toping.communicate()[0]
	hostalive = toping.returncode
	if hostalive == 0:
		print(i, 'Available')

	elif(i == '192.168.1.20'):
		break

	else:
		print(i, 'Unavailable')

	
