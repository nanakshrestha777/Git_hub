


import calendar

year = int(input("enter the number to check leap year:"))

result = calendar.isleap(year)

if (result):
    print("{0} is a leap year.".format(year))

else:
    print("{0} is not a leap year.".format(year))
    # # .isleap returns True for leap years, False for non-leap years.

# output:enter the number to check leap year:2026
# 2026 is not a leap year.

