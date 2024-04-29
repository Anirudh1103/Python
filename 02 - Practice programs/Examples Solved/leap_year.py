#Python Program to Check Leap Year

''' logic
if year % 400 == 0 and year % == 0 or  year % 4 == 0 year % 100 != 0'''

y = int(input("Enter a year to check if it is leap year or not: "))
if ((y % 400 == 0) and (y % 100 == 0)) or ((y % 4 == 0) and (y % 100 != 0)):
    print(str(y) + " is a leap year")
else:
    print(str(y) + " is not a leap year")