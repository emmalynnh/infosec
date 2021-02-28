#!/usr/bin/env python3

import sys, socket, errno, argparse, re, os.path
from socket import error as socket_error
from os import path

# variables and settings
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 3306, 3389]


# functions

# try to connect
def testconnect(srvconf):
	try:
		sock.connect(server_address)
		print("%s open" % port)
		sock.close()		
	except socket.timeout:
		print("%s timeout" % port)
	except socket_error as serr:
		if serr.errno == errno.ECONNREFUSED:
			print("%s closed" % port)
		if serr.errno != errno.ECONNREFUSED:
			raise serr

parser = argparse.ArgumentParser(description='Scan common ports on IPv4 address')
parser.add_argument('ipaddress', help="IPv4 address")
parser.add_argument('--timeout', '-t', type=int, help="Set connection timeout in seconds", default="6")
parser.add_argument('--version', '-v', action="version", version="%(prog)s 1.0")

args = parser.parse_args()

aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",args.ipaddress)

timeout = args.timeout

if aa:
	addr = args.ipaddress
	print('Host/IP: %s' % addr)
	# iterate over ports
	for port in ports:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.settimeout(timeout)
		server_address = (addr, port)
		testconnect(server_address)
elif not aa and path.exists(args.ipaddress):

	with open(args.ipaddress) as f:
		for line in f:
			parts = line.split()
			print(parts)
			if len(parts) > 1:
				addr = parts[1]

				print('Host/IP: %s' % addr)

				# iterate over ports
				for port in ports:
					sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					sock.settimeout(timeout)
					server_address = (addr, port)
					testconnect(server_address)
				


else:
	sys.exit("Please enter valid input")

