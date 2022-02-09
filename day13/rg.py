# Regular expression


import re

mystr = '''String is a collection of alphabets, words or other characters. It is one of the primitive data structures 
and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 
"immutable" which means they cannot be changed after they are created aii thth 91-45678
'''
# MetaCharacters
# [] . ^ $ * + ? {} () \ |

# pattern = re.compile(r'for') # searches for the index of the specified string
# pattern = re.compile(r'.')  #returns the matches for all characters
# pattern = re.compile(r'.ing') #retuns matches of string contain ING
# pattern = re.compile(r'^string') #returns result if the string starts with a specified string
# pattern = re.compile(r'created$') #returns result if the string ends with a specified string
# pattern = re.compile(r'co*') #returns occurrences of 'o'(zero or more of 'o')
# pattern = re.compile(r'co+')  #returns occurrences of 'o'(one or more of 'o')
# pattern = re.compile(r'st{2}')  # returns the occurrences of 't'times
# pattern = re.compile(r'(th){2}')  # return group of occurrences

# Special sequence
# \A,\b,\B,

#pattern = re.compile(r'\AString')  # returns match if specified string is at the start.
#pattern = re.compile(r'\bth') #returns match if the string is present in the in the word
#pattern = re.compile(r'\d{2}-\d{5}')
result = pattern.finditer(mystr)
for i in result:
    print(i)

# print(mystr[296:297])


# findall,search,split,sub,__finditer
