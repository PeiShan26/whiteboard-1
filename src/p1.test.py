def sorting():
    #Prompt user to enter a list of numbers
    unordered_numbers = input("Input: ")
    #Split the input strings into individual numbers
    numbers = [int(num) for num in unordered_numbers.split(", ")]
    #Sort the numbers in an ascending order
    sorted_numbers = sorted(numbers)
    return sorted_numbers

sorted_numbers = sorting()
#Display the ordered list
print("Sorted numbers: ", sorted_numbers)