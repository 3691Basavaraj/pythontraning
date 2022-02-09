
class BalanceCheckError(Exception):
    pass

def checkBalance():
    money=10000
    withdraw=11000
    balance=money-withdraw
    if(balance<2000):
        raise BalanceCheckError("You cannot withdraw amount")
    print(balance)

try:
    checkBalance()

except BalanceCheckError as  be:
    print(be)