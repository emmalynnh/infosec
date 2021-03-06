#!/usr/bin/env python3

import sys, socket, errno, argparse, re, os.path
from socket import error as socket_error
from os import path

# variables
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 3306, 3389]

# create and set arguments
parser = argparse.ArgumentParser(description='Scan common ports on IPv4 address')
parser.add_argument('ipaddress', help="IPv4 address")
parser.add_argument('--timeout', '-t', type=int, help="Set connection timeout in seconds", default="6")
parser.add_argument('--verbose', '-V', action="store_true", help="Verbose")
parser.add_argument('--version', '-v', action="version", version="%(prog)s 1.0")

# functions

# try to connect
def testconnect():
	print('IP: %s' % addr)
	# iterate over ports
	for port in ports:
		try:
			server_address = (addr, port)
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.settimeout(timeout)
			sock.connect(server_address)
			print("%s open" % port)
			sock.close()		
		except socket.timeout:
			if args.verbose:
				print("%s timeout" % port)
		except socket_error as serr:
			if serr.errno == errno.ECONNREFUSED and args.verbose:
				print("%s closed" % port)
			if serr.errno != errno.ECONNREFUSED:
				raise serr

# parse arguments
args = parser.parse_args()
timeout = args.timeout

# IPv4 Regex
aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",args.ipaddress)

# reader either IP or file given
if aa:
	addr = args.ipaddress
	testconnect()
elif not aa and path.exists(args.ipaddress):
	with open(args.ipaddress) as f:
		for line in f:
			parts = line.split()
			if len(parts) > 1:
				for part in parts:
					bb = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",part)
					if bb:
						addr = part
						testconnect()
else:
	sys.exit("Please enter valid input")