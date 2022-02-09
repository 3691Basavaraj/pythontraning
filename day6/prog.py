# Add three lists using map and lambda
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = [9,8,4,6,5]
result = map(lambda x, y, z: x + y + z, list1, list2, list3)
print(list(result))

#separate the odd and even numbers in a list

a = [2, 5, 7, 8, 10, 13, 16]
even = filter(lambda x: x % 2 == 0, a)
odds = filter(lambda x: x % 2 == 1, a)
print(list(even))
print(list(odds))

a = []
c = list((1,2,3,4,5))
print(a)
print(c)
b = [12, 24, 64, 1, 23, 76, 45, 32, 54, 67, 85]
div_three = filter(lambda x: x % 3 == 0, b)
print(list(div_three))

print(type(div_three))