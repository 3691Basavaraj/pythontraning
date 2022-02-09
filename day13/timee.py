import time

# 1.time() :- This function is used to count the number of seconds elapsed since the epoch.
'''print("Seconds elapsed since the epoch are : ")
print(time.time())'''

# 2.gmtime(sec) :- This function returns a structure with 9 values each representing a time attribute in sequence.
# using gmtime() to return the time attribute structure
'''print ("Time calculated acc. to given seconds is : ")
print (time.gmtime())'''

# 3.asctime(“time”) :- This function takes a time attributed string produced by gmtime() and returns a 24 character
# string denoting time. initializing time using gmtime()
#ti = time.gmtime()
# using asctime() to display time acc. to time mentioned
'''print("Time calculated using asctime() is : ", end="")
print(time.asctime())'''

# 4.ctime(sec) :- This function returns a 24 character time string but takes seconds as argument and computes time
# till mentioned seconds. If no argument is passed, time is calculated till present. using ctime() to display time
# string using seconds
print("Time calculated using ctime() is : ", end="")
print(time.ctime(20))

# 5.sleep(sec) :- This method is used to halt the program execution for the time specified in the arguments.
# sleep() method

print("Start Execution : ", end="")
print(time.ctime())

time.sleep(8)

print("Stop Execution : ", end="")
print(time.ctime())
