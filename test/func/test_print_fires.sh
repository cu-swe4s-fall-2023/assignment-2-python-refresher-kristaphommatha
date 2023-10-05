test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run working_output_no_operation python ../../src/print_fires.py --file_name data/test_data.csv --qc 2 --qv 'Afghanistan' --rc 6
assert_in_stdout "Output List"
assert_exit_code 0

run working_output_mean python ../../src/print_fires.py --file_name data/test_data.csv --qc 2 --qv 'Afghanistan' --rc 6 --op mean
assert_in_stdout "309"
assert_exit_code 0

run working_output_median python ../../src/print_fires.py --file_name data/test_data.csv --qc 2 --qv 'Afghanistan' --rc 6 --op median
assert_in_stdout "291"
assert_exit_code 0

run working_output_stdev python ../../src/print_fires.py --file_name data/test_data.csv --qc 2 --qv 'Afghanistan' --rc 6 --op stdev
assert_in_stdout "104"
assert_exit_code 0

run error_unknown_file python ../../src/print_fires.py --file_name DoesNotExist.csv --qc 2 --qv 'Afghanistan' --rc 6
assert_exit_code 1

chmod -r data/test_data.csv
run error_permission python ../../src/print_fires.py --file_name data/test_data.csv --qc 2 --qv 'Afghanistan' --rc 6
assert_exit_code 2

chmod +r data/test_data.csv
run error_exceeding_index python ../../src/print_fires.py --file_name data/test_data.csv --qc 20 --qv 'Afghanistan' --rc 6
assert_exit_code 3

run error_broken_column python ../../src/print_fires.py --file_name data/test_data.csv --qc 1 --qv 'Afghanistan' --rc 4
assert_exit_code 4