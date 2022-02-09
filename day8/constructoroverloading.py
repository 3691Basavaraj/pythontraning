'''Contructor overloading?
    .Python does not support explicit multiple constructors
    If multiple __init__ methods are written for the same class, then the latest one overwrites all the previous constructors.
Example:'''
class example:

    def __init__(self):
        print("One")

    def __init__(self):
        print("Two")

    def __init__(self):
        print("Three")

e = example()

'''
1.Overloading constructors based on arguments.
    The constructor overloading is done by checking conditions for the arguments passed and performing required actions.
Example:'''


def __init__(self, *args):

    if len(args) > 1:
        self.ans = 0
        for i in args:
            self.ans += i

    elif isinstance(args[0], int):
        self.ans = args[0] * args[0]

    elif isinstance(args[0], str):
        self.ans = "Hello! " + args[0] + "."


s1 = isinstance(1, 2, 3, 4, 5)
s2 = isinstance(5)
s3 = isinstance("Tibilsolution")

'''2.Calling methods from __init__.
    .A class can have one constructor __init__ which can perform any action when the instance of the class is created. 
    .This constructor can be made to different functions that carry out different actions based on the arguments passed
Example:'''


class eval_equations:

    def __init__(self, *inp):

        if len(inp) == 2:
            self.ans = self.eq2(inp)

        elif len(inp) == 3:
            self.ans = self.eq1(inp)

        else:
            self.ans = self.eq3(inp)

    def eq1(self, args):
        x = (args[0] * args[0]) + (args[1] * args[1]) - args[2]
        return x

    def eq2(self, args):
        y = (args[0] * args[0]) - (args[1] * args[1])
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = temp
        return z


inp1 = eval_equations(1, 2)
inp2 = eval_equations(1, 2, 3)
inp3 = eval_equations(1, 2, 3, 4, 5)

print("equation 2 :", inp1.ans)
print("equation 1 :", inp2.ans)
print("equation 3 :", inp3.ans)

'''3.Using @classmethod decorator.
    .This decorator allows a function to be accessible without instantiating the class. The functions can be 
    accessed both by the instance of the class and the class itself.
    .The first parameter of the method that is declared as classmethod is cls, 
    which is like the self of the instance methods. Here cls refer to the class itself. 
Example:'''
class eval_equations:
    def __init__(self, a):
        self.ans = a

    @classmethod
    def eq1(cls, args):
        # create an object for the class to return
        x = cls((args[0] * args[0]) + (args[1] * args[1]) - args[2])
        return x

    @classmethod
    def eq2(cls, args):
        y = cls((args[0] * args[0]) - (args[1] * args[1]))
        return y

    @classmethod
    def eq3(cls, args):
        temp = 0

        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / max(args)
        z = cls(temp)
        return z

li = [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]
i = 0

while i < 3:

    inp = li[i]

    if len(inp) == 2:
        p = eval_equations.eq2(inp)
        print("equation 2 :", p.ans)

    elif len(inp) == 3:
        p = eval_equations.eq1(inp)
        print("equation 1 :", p.ans)

    else:
        p = eval_equations.eq3(inp)
        print("equation 3 :", p.ans)

    # increment loop
    i += 1

