#!/usr/bin/env python3
import ipaddress
from subprocess import Popen, PIPE
import re
#import arpreq
import urllib.request as urllib2
import json
import codecs

url = 'http://macvendors.co/api/'
network = ipaddress.ip_network('192.168.1.0/24')

print('©2018 Vikendu Singh')
print('Version 1.7_rc9\nFeel free to share with others\n')
print('Checking first 20 IPs in your Subnet...  255.255.255.0 ... \n')

for i in network.hosts():

	i = str(i)

	toping = Popen(['ping', '-c','1',i], stdout = PIPE)
	output = toping.communicate()[0]
	hostalive = toping.returncode

	if hostalive == 0:

		print(i, 'Available')

		if(i == '192.168.1.1'):
			print('Your Network Administrator')

		#pid = Popen(["arp", "-n", i], stdout = PIPE)

		pid = Popen(["ip", "neigh", "show", i], stdout = PIPE)
		s = pid.communicate()[0].decode("utf-8")

		mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s)
		
		if mac is None:

			print("Your Device\n\n")

			#Uncomment the following to get your Device MAC and Manufacturer
			#Only works on kernels with ARP support(also uncomment the import)

			#request = urllib2.Request(url+mac, headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
			#response = urllib2.urlopen(request)
			#reader = codecs.getreader("utf-8")
			#obj = json.load(reader(response))
			
			#print (obj['result']['company']+"\n\n");

			continue

		else:
			mac = mac.groups()[0]

			print('Physical ID: ',mac)

			request = urllib2.Request(url+mac, headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
			response = urllib2.urlopen(request)
			reader = codecs.getreader("utf-8")
			obj = json.load(reader(response))

			print (obj['result']['company']+"\n\n");

	
	elif(i == '192.168.1.20'):
		break

	else:
		print(i, 'Unavailable\n\n')