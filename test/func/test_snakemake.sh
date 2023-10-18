test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

cd ../../data_presentations
run test_pngs snakemake --cores all
cd pngs
assert_equal Afghanistan.png $ls Afghanistan.png
assert_equal Croatia.png $ls Croatia.png
assert_equal Portugal.png $ls Portugal.png