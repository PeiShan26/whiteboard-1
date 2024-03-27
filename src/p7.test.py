def squareRoot(x):
    # Initial guess for the square root
    guess = x // 2
    # Iterate until the guess converges
    while guess * guess != x:
        # Improve the guess using the Babylonian method
        guess = (guess + x // guess) // 2
    return guess

x = int(input("Enter an integer: "))
print("Square root of", x, ":", squareRoot(x))

#Babylonian method: 1. Make an initial guess. | 2. Improve the guess. | 3. Iterate until convergence.
