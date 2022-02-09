class BankException(Exception):

    def __init__(self,bal, message="Balance is not sufficient"):
        self.bal = bal
        self.message = message
        super().__init__(self.message)


balance = 5000
withDrawAmount = int(input("Enter the amount to withdrawn: "))

try:
    if withDrawAmount > balance:
        raise BankException(withDrawAmount)
    else:
        print("Updated balance is: ", balance - withDrawAmount)
except BankException as e:
    print(e)
except Exception as e:
    raise BankException(e)
else:
    print("Withdrawal successful!")
finally:
    print("Exiting the program")
