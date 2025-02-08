# Recursion

# Recursion error

def recursive_function():
    print("I can do this forever ;)")
    recursive_function()

# recursive_function()

# Exit condition

def countdown(number):
    if number == 0:
        print("Blast off!")
    else:
        print(number)
        number -= 1
        countdown(number)

# countdown(10)

# Factorial

factorial_of_five = 5 * 4 * 3 * 2 * 1
print(f"Factorial of five: {factorial_of_five}")

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# print(factorial(5))  # try 20

# Add variables and print statements to log state each time the function gets called

def factorial(number):
    print(f"Called with {number}")
    if number == 0:
        print("Return 1")
        return 1
    else:
        factorial_of_next_lowest_number = factorial(number - 1)
        factorial_value = number * factorial_of_next_lowest_number
        print(f"Called with {number} returns {number} * {factorial_of_next_lowest_number} == {factorial_value}")
        return factorial_value

# print(factorial(5))

# Fibonnaci

def fibonacci(n):
    """ compute the nth Fibonacci number """

    if n < 0:  # check for negative number -- just in case.
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# nth values with zero-based index:
# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13

fibonacci(0)
