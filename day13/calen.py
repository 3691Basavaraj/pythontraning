import calendar
#1. calendar(year, w, l, c):- This function displays the year, the width of characters, no. of lines per week, and column separations.
# using calendar to print calendar of year
# prints calendar of 2012
'''print("The calendar of year 2022 is : ")
print(calendar.calendar(2012))
'''
#2. firstweekday() :- This function returns the first week day number. By default 0 (Monday).
# using firstweekday() to print starting day number   ASK
#calendar.setfirstweekday(4)
'''print("The starting day number in calendar is : ", end="")
print(calendar.firstweekday())'''


#3. isleap (year):- This function checks if the year mentioned in the argument is a leap or not.
'''if (calendar.isleap(2000)):
    print("The year is leap")
else:
    print("The year is not leap")'''

#4. leapdays (year1, year2):- This function returns the number of leap days between the specified years in arguments.
'''print("The leap days between 1950 and 2000 are : ", end="")
print(calendar.leapdays(1960, 2000))
'''
#5. month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments.
#   It takes 4 arguments, year, month, width of characters and no. of lines taken by a week.
# using month() to display month of specific year
'''print ("The month 5th of 2016 is :")
print (calendar.month(2022,5,2,1))'''


#6. monthrange(year, month) :- This function returns two integers, first, the starting day number of week(0 as monday) ,
 #second, the number of days in the month.
# using monthrange() to print start week day and
# number of month
'''print("The start week number and no. of days of month : ", end="")
print(calendar.monthrange(2022, 1))'''

#7.prcal(year, w, l, c) :- This function also prints the calendar of specific year but there is no need of “print” operation to execute this.
# using prcal() to print calendar of 1997
'''print("The calendar of 1997 is : ")
calendar.prcal(2022, 2, 1, 6)'''


#8. prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need of “print” operation to execute this.
# using prmonth() to print calendar of 1997
'''print("The 4th month of 1997 is : ")
calendar.prmonth(1997, 4, 2, 1)
'''

#9. setfirstweekday(num) :- This function sets the day start number of week.
# using setfirstweekday() to set first week day number
'''calendar.setfirstweekday(4)'''


# using firstweekday() to check the changed day
'''print("The new week day number is : ", end="")
print(calendar.firstweekday())'''

#10.weekday(year, month, date) :- This function returns the week day number(0 is Monday) of the date specified in its arguments.

# using weekday() to print day number of date
print ("The day number of 25 April 1997 is : ",end="")
print (calendar.weekday(2022,1,24))
