'''time module
.time() :- This function is used to count the number of seconds elapsed since the epoch.
.gmtime(sec) :- This function returns a structure with 9 values each representing a time attribute in sequence.
It converts seconds into time attributes(days, years, months etc.) till specified seconds from epoch.
If no seconds are mentioned, time is calculated till present.
.asctime(“time”) :- This function takes a time attributed string produced by gmtime() and returns a 24 character string denoting time.
. ctime(sec) :- This function returns a 24 character time string but takes seconds as argument and computes time till mentioned seconds.
 If no argument is passed, time is calculated till present.
.sleep(sec) :- This method is used to halt the program execution for the time specified in the arguments.

Operations on Date :

1. MINYEAR :- It displays the minimum year that can be represented using date class.

2. MAXYEAR :- It displays the maximum year that can be represented using date class.


3. date(yyyy-mm-dd) :- This function returns a string with passed arguments in order of year, months and date.

4. today() :- Returns the date of present day in the format yyyy-mm-dd.
5. fromtimestamp(sec) :- It returns the date calculated from the seconds elapsed since epoch mentioned in arguments.

6. min() :- This returns the minimum date that can be represented by date class.

7. max() :- This returns the maximum date that can be represented by date class.



Calendar module
1. calendar(year, w, l, c):- This function displays the year, the width of characters, no. of lines per week, and column separations.
2. firstweekday() :- This function returns the first week day number. By default 0 (Monday).
3. isleap (year):- This function checks if the year mentioned in the argument is a leap or not.
4. leapdays (year1, year2):- This function returns the number of leap days between the specified years in arguments.
5. month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments.
It takes 4 arguments, year, month, width of characters and no. of lines taken by a week.
6. monthrange(year, month) :- This function returns two integers, first, the starting day number of week(0 as monday) ,
 second, the number of days in the month.
7.prcal(year, w, l, c) :- This function also prints the calendar of specific year but there is no need of “print” operation to execute this.
8. prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need of “print” operation to execute this.
9. setfirstweekday(num) :- This function sets the day start number of week.
10.weekday(year, month, date) :- This function returns the week day number(0 is Monday) of the date specified in its arguments.


datetime::
The DateTime module is categorized into 6 main classes –

1.date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect.
    Its attributes are year, month and day.
3.time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds.
    Its attributes are hour, minute, second, microsecond, and tzinfo.
4.datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
5.timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
6.tzinfo – It provides time zone information objects.
7.timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC
'''