#program to compute the maturity amount 
p = int(input("Enter the principle amount: "))
r = float(input("Enter the rate opf intrest: "))
n = int(input("Enter the number of times intrest is computed every year: "))
t = int((input("Enter the number of times deposited ")))
A = p*(1 + (r/n))**(n*t)
print("Maturity amount: ",round(A))