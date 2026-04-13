# 16 - Functions - Lambda functions and Recursion functions

```python
# Lambda function

'''
--> A lambda function in Python is a small anonymous (nameless) function used for short, simple operations.
--> A lambda function is a one-line function defined without using the def keyword and with lambda keyword.


Key Characteristics
--> Anonymous (no function name)
--> Defined using lambda keyword
--> Can take any number of arguments
--> Contains only one expression
--> Returns value automatically (no return keyword needed)
--> Used for short and simple operations

Advantages
--> Reduces code length
--> Useful for temporary functions
--> Commonly used with functions like map(), filter(), sorted()

Syntax
lambda arguments : expression
```

```python
# Example 1: Addition

add = lambda a, b: a + b
print(add(5, 3))
```

```python
# Example 2: Square of a Number

square = lambda x: x * x
print(square(4))
```

```python
# Example 3: Lambda without Variable

print((lambda x: x + 10)(5))
```

```python
# Example 4: Using with map()

nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
print(result)
```

```python
# Example 5: Using with filter()

nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
```

```python
# Recursion function

'''
Recursion is a programming technique where a function calls itself to solve a smaller or simpler version of a problem.

Key Points

Recursive function → A function that calls itself.
Base case → Condition that stops recursion. Without it, the function would run infinitely (causing stack overflow).
Use cases → Problems like factorial, Fibonacci series, tree traversal, searching, etc.     

Advantages of Recursion

--> Makes code cleaner and easier to read.
--> Solves complex problems naturally (like tree traversal).
--> Implements divide-and-conquer algorithms efficiently.

Disadvantages of Recursion

--> Uses more memory (function calls are stacked).
--> Can be slower than iteration.
--> Needs a base case, or it leads to infinite recursion.

'''

# General form of a recursive function:

def recursive_function(parameters):
    if base_condition_met:
        return base_value         # Base case
    else:
        return recursive_function(smaller_parameters) # Recursive call
```

```python
''' 
Example 1: Factorial of a Number

The factorial of n (n!) is the product of all positive integers from 1 to n

n!=n×(n−1)×(n−2)…1

Recursive Formula :-    factorial(n)=n×factorial(n−1)

Base Case formula :-     factorial(0)=1

'''

def factorial(n):
    if n == 0:            # Base case
        return 1
    else:
        return n * factorial(n-1)  # Recursive call

# Test the function
print(factorial(5))
```

```python
'''
Example 2: Fibonacci Series

The Fibonacci series: 0, 1, 1, 2, 3, 5, 8 ...

Recursive Formula:-  fib(n)=fib(n−1)+fib(n−2)

Base Case formula :-  fib(0)=0,fib(1)=1

'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first 7 Fibonacci numbers
for i in range(7):
    print(fibonacci(i), end=" ")
```
