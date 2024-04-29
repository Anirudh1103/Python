#Python Program to Check if a Number is Odd or Even

x = int(input("Enter the number to Check if a Number is Odd or Even: "))
if x % 2 == 0:
    print(str(x) + " is even")
else:
    print(str(x) + " is odd")