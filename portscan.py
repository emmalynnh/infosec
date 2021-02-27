#!/usr/bin/env python3

import sys, socket, errno
from socket import error as socket_error

# variables and settings
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 3306, 3389]

# functions

# try to connect
def testconnect(srvconf):
	try:
		sock.connect(server_address)
		print("%s accepted" % port)
		sock.close()		
	except socket.timeout:
		print("%s timeout" % port)
	except socket_error as serr:
		if serr.errno == errno.ECONNREFUSED:
			print("%s rejected" % port)
		if serr.errno != errno.ECONNREFUSED:
			raise serr

print('\nCommon Port Scanner\n')
print('Ports: %s\n' % ports)
print('Timeout: 6 seconds')
# Research better ways to do below
# Grab argument and assign it a variable
if len(sys.argv) < 2:
	print('Please provide Host/IP')
	sys.exit()
for arg in enumerate(sys.argv):
	addr = arg[1]
print('Host/IP: %s' % addr)
# iterate over ports
for port in ports:
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(6)
	server_address = (addr, port)
	testconnect(server_address)