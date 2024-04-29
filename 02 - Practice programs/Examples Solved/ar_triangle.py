#python program to write area of triangle
a = float(input("Enter the first side of triangle"))
b = float(input("Enter the second side of the triangle"))
c = float(input("Enter the third side of the triangle"))
s = (a + b +  c)/2
area = (s*(s-a) * (s-b) * (s-c)) ** 0.5 #**0.5 is for sqrt

print("Area of Tringle = " + str(area))