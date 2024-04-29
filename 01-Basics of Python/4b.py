li_tuples = [(4,5),(2,3),(6,7),(2,8)]
print("The original list of tuples are:")
print(li_tuples)

li_tuples.sort(key=lambda x:x[0]+x[1])
print("Sorted list of tuples based on their sum is", li_tuples)