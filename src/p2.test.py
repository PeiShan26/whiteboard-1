def fizzBuzz():
    #Use for loop for iterating over a sequence
    for num in range(1, 101):
        #To check if the number is divisible by both 3 and 5
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        # To check if the number is divisible by 3
        elif (num % 3 == 0):
            print("Fizz")
        # To check if the number is divisible by 5
        elif (num % 5 == 0):
            print("Buzz")
        else:
            print(num)

#Call the function
fizzBuzz()