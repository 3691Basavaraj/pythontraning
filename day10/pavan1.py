class UnderageException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OverageException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


a = int(input("enter the age: "))
try:
    if a < 18:
        e = UnderageException("you are under age to apply for DL")
        raise e
    elif a > 60:
        e = OverageException("you are over age to apply for DL")
except
