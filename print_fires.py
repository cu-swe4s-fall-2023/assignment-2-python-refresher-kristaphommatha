import my_utils as utils
import sys

flag = int(sys.argv[1])
country= sys.argv[3]
county_column = int(sys.argv[2])
result_column = int(sys.argv[4])
file_name = 'Agrofood_co2_emission.csv'

if flag == 0:
    fires = utils.get_column(file_name,county_column,country)
elif flag == 1:
    fires = utils.get_column(file_name,county_column,country,result_column)
else:
    print('Invalid input')
    

print(fires)
