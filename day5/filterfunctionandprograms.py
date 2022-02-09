'''Filter function?
    The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.

    Syntax:
        filter(function, iterable)'''

#Example:

#to filter vowels
'''letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
filtered_vowels = filter(filter_vowels, letters)
vowels = tuple(filtered_vowels)
print(vowels)'''

#using none as a parameter
'''random_list = [1, 'a', 0, False, True, '0']
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)'''


#program to filter even number in a list with filter and lambda function

'''numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers = filter(lambda x: (x%2 == 0), numbers)
even_numbers = list(even_numbers)
print(even_numbers)'''

#program to filter even number in a list without filter and lambda function

'''list = [1, 2, 3, 4, 5]
list2 = [i for i in list if i % 2 == 0]
print(list2)'''