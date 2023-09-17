#!/bin/bash
set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

echo "Opening Agrofood_co2_emission.csv and searching column 1 for Afghanistan and outputting results from column 4"
python print_fires.py --file_name Agrofood_co2_emission.csv --qc 1 --qv 'Afghanistan' --rc 4

echo "Opening DoesNotExist.csv and searching column 1 for Afghanistan and outputting results from column 4"
python print_fires.py --file_name DoesNotExist.csv --qc 1 --qv 'Afghanistan' --rc 4

echo "Opening Agrofood_co2_emission.csv and searching column 100 for Afghanistan and outputting results from column 4"
python print_fires.py --file_name Agrofood_co2_emission.csv --qc 100 --qv 'Afghanistan' --rc 4