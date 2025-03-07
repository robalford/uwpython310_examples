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

# Fibonnaci Series

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

print(fibonacci(0))  # fib(0) = 0
print(fibonacci(1))  # fib(1) = 1  # after this, can refer back to the previous Fibonnaci return values each time
print(fibonacci(2))  # fib(2-1) + fib(2-2) = 1
print(fibonacci(3))  # fib(3-1) + fib(3-2) = 2
print(fibonacci(4))  # fib(4-1) + fib(4-2) = 3
print(fibonacci(5))  # fib(5-1) + fib(5-2) = 5
print(fibonacci(6))  # fib(6-1) + fib(6-2) = 8
print(fibonacci(7))  # fib(7-1) + fib(7-2) = 13
