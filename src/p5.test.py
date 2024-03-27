def difference(list1, list2):
    #To store common elements between two lists
    difference = []
    for num1 in list1:
        if num1 not in list2 and num1 not in difference:
            difference.append(num1)
    for num2 in list2:
        if num2 not in list1 and num2 not in difference:
                #Add num1 into the 'intersection' list
                difference.append(num2)
    return difference

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
print("List 1: ", list1)
print("List 2: ", list2)
#Display the 'intersection' list by calling the function
print("Symmetric difference:", sorted(difference(list1, list2)))