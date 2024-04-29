import numpy as np
names = np.array(['John','David','Smith'])
height = np.array([1.5,1.78,1.6])
weight = np.array([65,46,59])
BMI = weight/height**2
print(BMI)
print("Overweight: ",names[BMI>=25])
print("Underweight: ",names[BMI<=18.5])
print("Healthy : ",names[(BMI>=18.5) & (BMI<=25)])