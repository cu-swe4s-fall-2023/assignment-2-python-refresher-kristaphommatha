#!/bin/bash
set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

a=$1
b=$2
c=$3
d=$4

echo "Searching column $b for $c and outputting results from column $d"
python3 print_fires.py $a $b $c $d