# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Diffrentiate between Julian and Gregorian Calanders

#!/bin/python3

import sys
from datetime import datetime, timedelta
# import julian

def solve(year):
    # Complete this function
    # dt = datetime((year-1), 12, 31)
    # dop_dt = (dt + timedelta(days=256)).strftime('%d.%m.%Y')
    # dop_dt_str = 
    # print(dop_dt)

	if(year < 1700):
		return "Please enter a vaild year from the range 1700 <= year <= 2700"
	elif(1700 <= year <= 1917):
		if(year % 4 == 0):
			return ('12.09.'+str(year))
		else:
			return ('13.09.'+str(year))
	elif(year == 1918):
		return ('26.09.'+str(year))
	elif(1918 < year <= 2700):
		if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
			return ('12.09.'+str(year))
		else:
			return ('13.09.'+str(year))
	else:
		return "Please enter a vaild year from the range 1700 <= year <= 2700"
		
	
year = int(input().strip())
result = solve(year)
print(result)
