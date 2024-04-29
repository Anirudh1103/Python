def grouping_dictionary(list1):
    result = {}
    for key,value in list1:
        result.setdefault(key,[]).append(value)
    return result

colors = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
print("listy of key and values: ")
print(colors)
print("Dictionaray of key and values: ")
print(grouping_dictionary(colors))