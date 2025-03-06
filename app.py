import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number!")
    return math.factorial(n)

if __name__ == "__main__":
    print(add(3,5))
    print(subtract(10,5))
    print(multiply(10,20))
    print(divide(100,5))
    print(power(2,3))
    print(modulus(10,5))
    print(square_root(625))
    print(factorial(5))