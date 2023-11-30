#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    operators = ["+", "-", "*", "/"]
    a = 10
    b = 5

    for operator, operation in zip(operators, [add, sub, mul, div]):
        result = operation(a, b)
        print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
