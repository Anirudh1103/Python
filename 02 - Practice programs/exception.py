try:
    a = int(input("enter the number"))
    print(10 + a)
except Exception as b:
    print("Error in user understandble way:")
    print("Error occoured\nplease run the program again and give valid input")

    print("Error captured by the program which is displayed in Technical words")
    print(b)
