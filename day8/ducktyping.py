'''Duck typing?
    The main reason for using duck typing is to provide support for dynamic typing in Python programming.
    In Python, we don't need to specify the variable's data type and we can reassign the different data
    type values to same variable in further code.
    The duck typing is the most appropriate style for the EAFP because we don't need to focus on the "type" of the object.
    We only need to take care of its behavior and capability.

Example:'''
x = 12000
print(type(x))

x = 'Dynamic Typing'
print(type(x))

x = [1, 2, 3, 4]
print(type(x))

#Example:


class VisualStudio:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Spell Check')
        print('Convention Check')

class Desktop:
    def code(self, ide):
        ide.execute()

ide = VisualStudio()
desk = Desktop()
desk.code(ide)



'''

'''