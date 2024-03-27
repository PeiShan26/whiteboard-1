def fibonacci(n):
    if n <= 0:
        #Return empty list as no Fibonacci numbers for non-positive integers
        return []
    elif n == 1:
        #The list only contains 0 which is the first Fibonacci number
        return [0]
    elif n == 2:
        #The list contains 0 and 1
        return [0, 1]
    else:
        #Recursively calls fibonacci(n-1) to generate sequence up to the (n-1)th term
        seq = fibonacci(n - 1)
        #Appends the sum of the last two elements of the sequence
        seq.append(seq[-1] + seq[-2])
        return seq

n = int(input("Enter a number: "))
print(fibonacci(n))