import time
t = time.strftime('%H:%M:%S')
print("Time: ",t)

th = int(time.strftime('%H'))
if (th >= 0) and (th<12):
    print("Good Morning")
elif (th>=12) and (th<18):
    print("Good afternoon")
elif (th>=18) and (th<20):
    print("Good evening")
else:
    print("Good night") 