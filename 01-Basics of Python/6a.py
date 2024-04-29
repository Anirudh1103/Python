#program to print a list of prime numbers
def is_prime(n):
    flag = True
    for f in range(2,n//2+1):
        if n%f == 0:
            flag = False
            break
    return flag
def list_of_prime(num):
    prime_list = []
    for n in range(2,num):
        if is_prime(n):
            prime_list.append(n)
    return prime_list
num = int(input("Enter a number to print a list of prime numbers: "))
print(list_of_prime(num))