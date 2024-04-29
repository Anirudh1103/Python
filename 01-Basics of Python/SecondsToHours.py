#program to convert given total seconds into hours min and seconds 
t_sec = int(input("Enter the total seconds: "))
hrs = t_sec//3600
r_sec = t_sec%3600
min = r_sec//60
sec = r_sec%60
print("Hrs: {0} Min: {1} Sec: {2}".format(hrs,min,sec))