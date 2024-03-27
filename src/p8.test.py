def anagram(str1, str2):
    #Remove the empty spaces and convert to lowercase
    str1 = str1.replace(" ", " ").lower()
    str2 = str2.replace(" ", " ").lower()

    #To check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

str1 = input("Input the first string: ")
str2 = input("Input the second string: ")

if anagram(str1, str2):
    print("True")
else:
    print("False")