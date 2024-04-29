a = int(input("Enter the value of first number"))
b = int(input("Enter the value of second number"))
ch = int(input("Enter your choice: \n1:Add\n2:Sub\n3:Mul\n4:Div"))

match ch:
    case 1:
        op = (a)+(b)
        print("Sum = " + str(op))
    case 2:
        op = (a) - (b)
        print("Diffrence = " + str(op))
    case 3:
        op = (a) * (b)
        print("Product = " + str(op))
    case 4:
        op = (a) / (b)
        print("Quotent = " + str(op))
    case _:
        print("Invalid choice")
