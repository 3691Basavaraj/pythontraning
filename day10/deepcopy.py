'''
1.A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
2.The deep copy creates independent copy of original object and all its nested objects.
3.Changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.
syntax:
import copy
copy.deepcopy(x)

Example:
'''
'''import copy

list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
list2 = copy.deepcopy(list1)

#list1[0][1] = 'a'

print(list1)
print(list2)'''


