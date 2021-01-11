#!/bin/bash
echo " "
echo " ------------------------------------------------"
echo " | TLD CHECK - Find all TLDs of domain provided |"
echo " ------------------------------------------------"
echo " "
echo " Usage: tld-check.sh [domain(.txt)]"
echo " "

IFS=$'\r' GLOBIGNORE='*' command eval 'OUTPUT=($(curl -s https://data.iana.org/TLD/tlds-alpha-by-domain.txt | sed "1d"))'

TLIST=($OUTPUT)

function read_file() {
	if [ -f "$1" ]; then
	IFS=$'\r' GLOBIGNORE='*' command eval 'OUTPUT=($(cat $1))'
	else
		OUTPUT=$1
	fi
}

read_file $1
DLIST=($OUTPUT)

for ((i=0; i<${#DLIST[@]}; i++)); do
	for ((a=0; a<${#TLIST[@]}; a++)); do
    	DNAME="${DLIST[$i]}.${TLIST[$a]}"
    	host ${DNAME} 1.1.1.1 | grep -i 'has address' | cut -d " " -f 1,4
    done
done


