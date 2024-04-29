#program to display the lost elemnts in a list using diffrence operation
def lost_elements(original, duplicate):
    original_set = set(original)
    duplicate_set = set(duplicate)
    return (original_set-duplicate_set)
list1 = [1,2,3,4,5]
list2 = [2,4,5]
print(list(lost_elements(list1,list2)))