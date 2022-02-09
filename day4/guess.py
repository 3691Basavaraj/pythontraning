'''num = int(input('Enter the Number:'))
rev_num=0

while(num>0):
    rev_num = rev_num*10 + num%10
    num = num//10
    print(rev_num)
else:
    print("Invalid Input")
    '''



in_string = input("Enter a Sentence: ")
str = in_string.lower()
print(str)
count = 0
list = ("a","e","i","o","u")
for char in str:
    if char in list:
        count = count+1
print("Number of vowels are:",count)









