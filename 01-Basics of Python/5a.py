def is_sub_list(list1, list2):
    if list2==[] or list2 == list1:
        sublist = True
    elif len(list2)>len(list1):
        sublist = False
    else:
        sublist = False
        for i in range(len(list1)-len(list2)+1):
            if list1[i] == list2[0]:
                j=1
                while(j<len(list2))and i+j<len(list1)and list1[i+j] == list2[j]:
                    j+=1
                if j == len(list2):
                    sublist = True
                    break

    return sublist
list1 = [int(item) for item in input("Enter the main list: ").split()]
list2 = [int(item) for item in input("Enter the sublist: ").split()]
print("Main list: ",list1)
print("Sublist: ",list2)
if is_sub_list(list1,list2):
    print(list2, " is sublist of ",list1)
else:
    print(list2, " is not a sublist of ",list1)