#program to find square root using newtons method

n = float(input("Enter the number whose square root needs to be found: "))
treshold = 0.01
approximation =n/2
while True:
    better = (approximation+n/approximation)/2
    if abs(approximation-better)<treshold:
        print(round(better))
        break
    approximation = better