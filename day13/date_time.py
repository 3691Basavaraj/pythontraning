# 1.The date class is used to instantiate date objects in Python. When an object of this class is instantiated,
# it represents a date in the format YYYY-MM-DD.

from datetime import date
from datetime import datetime
import datetime

# initializing constructor
# and passing arguments in the
# format year, month, date
'''my_date = date(1996, 12, 13)

print("Date passed as argument is", my_date)'''

# 2.To return the current local date today() function of date class is used. today() function comes with several
# attributes (year, month and day).

'''today = date.today()

print("Today's date is", today)'''

# 3.to get year, month, and date attributes from the date object using the year, month and date attribute of the date
# class.

'''today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)'''

# 5.We can convert date object to a string representation using two functions isoformat() and strftime().

'''today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
'''


# display the current date:
'''x = datetime.datetime.now()
print(x)'''

# Return the year and name of weekday:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%a"))

# Display the name of the month:using strftime()
'''x = datetime.datetime(2022, 1, 31)

print(x.strftime("%D"))'''
