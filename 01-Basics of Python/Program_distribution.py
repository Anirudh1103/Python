# Import the random module
import random
import os
import time
import programlist
# Create an empty dictionary
user_numbers = {}
# Ask the user how many entries they want to make
n = int(input("How many entries do you want to make? "))
# Loop through the number of entries
for i in range(n):
  # Ask the user to enter a name
  name = input("Enter a name: ")
  # Generate a random number between 1 and 100
  random_number = random.randrange(1, 11)
  if random_number==1:
    print("""1a) write a python program to convert the given number of seconds to hours,minutes,and seconds and display the result""")
    print("""1b) write a python program to compute and display the maturity for the deposit made in abank by applying compound intrest""" )
if random_number==2:
    print("""2 a) Write a Python program that uses Newtons method to find the square root of a given
        number""")
    print("""(2 b) Write a Python program that generates multiplication table of given size using nested forloops""")
if random_number==3:
    print("""3a Write a Python program with a user defined function to draw multi coloured squares of
        given size using turtle graphics""")
    print("""3 b) Write a Python program to compute the sum of the elements in a list using your own logicand also by calling the built-in sum function. Compute and display the time taken to find the
        sum in both the methods (Use time module)""")
if random_number==4:
    print("""4 a) Write a Python program to read a phrase, remove all punctuations in the phrase and
        display the phrase along with the list of words in the phrase""")
    print("""4b) Write a Python program to sort a list of tuples based on the sum of elements in the tuple Use lambda function to generate the key for sorting""")
if random_number==5:
    print("""5 a) Write a Python program that reads two integer lists from the user and checks whether list2is a sub list of list1 or not.""")
    print("""5 b) Write a Python program that groups a list of key-value pairs into a dictionary of lists """)
if random_number==6:
    print("""6 a) Write a Python program that generates and prints a list of prime numbers less than the
        given number. """)
    print(""" 6 b) Write a Python program to display the lost elements in a duplicate list using set difference
        operation.""")
if random_number==7:
    print("""7 a) Write a Python program to copy the contents of a source file to a destination file by
        omitting comment lines (lines that start with #). """)
    print("""7 b) Write a Python program to draw a Polygon of given number of sides. The program should
        raise appropriate exception when the number of sides is negative or zero. """)
if random_number==8:
    print("""8 a) Write a Python program to store the names, heights in meters and weights in kilograms of agroup of people in three NumPy arrays, compute the Body Mass Index (BMI) of these group of people and classify them as underweight, overweight or healthy based on the following conditions:
         Underweight, if BMI < 18.5
         Overweight, if BMI > 25
         Healthy, if 18.5 <= BMI <= 25
        Where, BMI=weight/height**2 """)
    print(""" 8 b) Write a Python program to store the names, ages and heights in meters of a group of
        people in three NumPy arrays, display the three arrays in the sorted order of their age.""")
if random_number==9:
    print(""" 9a) Write a Python program to create a DataFrame from a Comma Separated Values file (.csv )
        consisting of Name, Score, Attempts and Qualified status.
        Perform the following operations using the DataFrame:
        i) Display the details of all the students
        ii) Display the details of first 3 students
        iii) Display the name and score of all the students
        iv) Display the details of qualified students
        v) Display the details of students who made more than one attempt
        vi) Display the mean score of students
        vii) Display student details in decreasing order of their scores""")
    print("""9b) Write a Python program to create a DataFrame from a dictionary that shows the gender of each person and the team to which the person belongs. Using crosstab, summarize the data and generate tables to show i) the distribution of genders in each team and ii) the distribution of
        teams for each gender. """)
if random_number==10:
    print(""" 10 a) Write a Python program to plot monthly rainfall using bar chart.""")
    print("""10 a) Write a Python program to plot monthly rainfall using bar chart. """)
else:
  print(random_number," experiment is allocates to",name,"experiment name=",programlist)
  #print(input("click enter to clear screen"))
  time.sleep(5)
  os.system('cls')
  # Assign the number to the name in the dictionary
  user_numbers[name] = random_number
# Print the dictionary
print(user_numbers)
