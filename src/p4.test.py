def intersection(list1, list2):
    #To store common elements between two lists
    intersection = []
    for num1 in list1:
        for num2 in list2:
            #To check if num1 is equal to num2 and it's not already present in the 'intersection' list
            if num1 == num2 and num1 not in intersection:
                #Add num1 into the 'intersection' list
                intersection.append(num1)
    return intersection

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
print("List 1: ", list1)
print("List 2: ", list2)
#Display the 'intersection' list by calling the function
print("Intersection:", intersection(list1, list2))