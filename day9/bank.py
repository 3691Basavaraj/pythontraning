class bankException(Exception):

    def __init__(self, msg="Enter a amount less than"):
        self.msg = msg


withdraw_amt = int(input("Enter the amount to be withdrawn"))
try:
    balance = 10000
    if withdraw_amt > balance:
        raise bankException("Insufficient balance")
except bankException as e:
    print(withdraw_amt, e.msg)



