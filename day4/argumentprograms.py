'''Python Default Arguments
       python lets user assign default value as arguments
       The default value is assigned using "=" operator
       Example:'''

def greet(name, msg="Good morning!"):
        print("Hello", name + ', ' + msg)
greet("abc")
greet("abc", "How are you?")

'''Python Keyword Arguments
    Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and an equal to sign
    assignment of value to the keyword is done explicitly.
Example:'''
'''def person_name(first_name, second_name):
  print(first_name + second_name)
person_name(first_name="Tibil", second_name="solution")'''