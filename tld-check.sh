#!/bin/bash
echo "------------------------------"
echo "|         TLD CHECK          |"
echo "------------------------------"
echo "| Usage: tld-check.sh [name] |"
echo "------------------------------"

if [ $# -eq 0 ]; then
	printf "Enter a name: "
	read -r DOMAIN
else
       DOMAIN=$1
fi

wget https://data.iana.org/TLD/tlds-alpha-by-domain.txt

FILE=tlds-alpha-by-domain.txt
if [ -f "$FILE" ]; then
	IFS=$'\r' GLOBIGNORE='*' command eval 'TLD=($(cat tlds-alpha-by-domain.txt))'
	#echo $TLD
	for i in $TLD
		do
			i="${DOMAIN}.${i}"
			#echo "$i"
			host ${i} | grep -i 'has address' | cut -d " " -f 1,4 
		done
	rm tlds-alpha-by-domain.txt
else
	echo "Error downloading TLD file."
fi