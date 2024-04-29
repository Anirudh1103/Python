#Python Program to Display the multiplication Table
x = int(input("Enter the number whose table you want to display: "))
i = 1
while i < 11:
    print(str(x) + " * " + str(i) + " = " + str(x * i))
    i = i + 1