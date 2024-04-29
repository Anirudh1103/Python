#Python Program to Find the Largest Among Three Numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
print("Entered numbers are: ")
print(x,y,z)

if ((x>y) and (x>z)):
    print(str(x) + " is greater")
elif((y>x) and (y>z)):
    print(str(y) + " is greater")
else:
    print(str(z) + " is greater")