class Calculator:
    def __init__(self):
        print("Calculator object successfuly initialized")
    
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    