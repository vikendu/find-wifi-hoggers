#!/usr/bin/env python3

import subprocess
import ipaddress
from subprocess import Popen, PIPE
import re
import arpreq
import urllib.request as urllib2
import json
import codecs

url = 'https://macvendors.co/api/'
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
		#Some Xiaomi devices return None
		if mac is None:

			#arpreq for Xiaomi devices
			mac = arpreq.arpreq(i)
			print(mac)

			request = urllib2.Request(url+mac, headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
			response = urllib2.urlopen(request)
			reader = codecs.getreader("utf-8")
			obj = json.load(reader(response))
			print (obj['result']['company']+"\n\n");

			continue

		else:
			mac = mac.groups()[0]
			print(mac)
			request = urllib2.Request(url+mac, headers={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
			response = urllib2.urlopen(request)
			reader = codecs.getreader("utf-8")
			obj = json.load(reader(response))
			print (obj['result']['company']+"\n\n");

	
	elif(i == '192.168.1.20'):
		break

	else:
		print(i, 'Unavailable\n\n')

	
