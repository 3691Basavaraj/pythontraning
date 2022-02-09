class bank:
    pass


class accno(bank):
    pass


class ROI(bank):
    pass


Accountno = 'active'
try:
    if Accountno == 'active':
        raise print('Account is active!')
    else:
        print('The account number does not Exist:')

except Exception:
    print("The ROI offered for the active count is...:")
else:
    print("No offers for the current account")

finally:
    print("Thank you!Visit again!")
