# Function Definitions

def greet(name):
    """Function to greet a person with their name."""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n < 0:
        return "Error! Factorial of a negative number doesn't exist."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def fibonacci(n):
    """Function to generate Fibonacci sequence up to n."""
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
if __name__ == "__main__":
    print(greet("Alice"))
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 0))
    print("Factorial of 5:", factorial(5))
    print("Fibonacci sequence up to 10:", fibonacci(10))