# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

import datetime

def count_sundays_on_first():
    count = 0
    # Iterate over the years in the twentieth century
    for year in range(1901, 2001):
        # Iterate over the months
        for month in range(1, 13):
            # Check if the first day of the month is a Sunday (weekday number 6)
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1

    return count

# Count the number of Sundays that fell on the first of the month
sunday_count = count_sundays_on_first()
print("The number of Sundays that fell on the first of the month during the twentieth century is:", sunday_count)
