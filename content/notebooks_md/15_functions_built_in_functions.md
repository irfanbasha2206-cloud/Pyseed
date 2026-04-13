# 15 - Functions - Built-in functions

```python
# Built-in functions in python

'''
Built-in functions are predefined functions in Python that are always available for use without importing any module.

--> They help perform common tasks easily.
--> They save time and reduce code complexity.
--> Can be used directly in any Python program.
--> Example:-                                                     '''

# All Common Built-in Functions with Examples in Python

'''

| Function         | Description                            | Example                              | Output                       |
| ---------------- | -------------------------------------- | ------------------------------------ | ---------------------------- |
| `abs()`          | Returns absolute value of a number     | `abs(-5)`                            | 5                            |
| `all()`          | Returns True if all elements are true  | `all([True,1,5])`                    | True                         |
| `any()`          | Returns True if any element is true    | `any([0,False,3])`                   | True                         |
| `ascii()`        | Returns ASCII representation of object | `ascii('A')`                         | `'A'`                        |
| `bin()`          | Converts integer to binary string      | `bin(10)`                            | `'0b1010'`                   |
| `bool()`         | Converts a value to boolean            | `bool(0)`                            | False                        |
| `bytearray()`    | Returns a mutable byte array           | `bytearray(3)`                       | `bytearray(b'\x00\x00\x00')` |
| `bytes()`        | Returns an immutable byte object       | `bytes(3)`                           | `b'\x00\x00\x00'`            |
| `callable()`     | Checks if object is callable           | `callable(len)`                      | True                         |
| `chr()`          | Returns character from ASCII/Unicode   | `chr(65)`                            | 'A'                          |
| `classmethod()`  | Creates a class method                 | Used in class                        | —                            |
| `compile()`      | Compiles source code                   | `compile('x=5','<string>','exec')`   | Code object                  |
| `complex()`      | Creates a complex number               | `complex(2,3)`                       | (2+3j)                       |
| `delattr()`      | Deletes an attribute from object       | `delattr(obj,'x')`                   | —                            |
| `dict()`         | Creates a dictionary                   | `dict(a=1,b=2)`                      | `{'a':1,'b':2}`              |
| `dir()`          | Lists attributes/methods of object     | `dir([])`                            | List of methods              |
| `divmod()`       | Returns quotient and remainder         | `divmod(10,3)`                       | (3,1)                        |
| `enumerate()`    | Returns index and value pairs          | `list(enumerate(['a','b']))`         | [(0,'a'),(1,'b')]            |
| `eval()`         | Evaluates a string expression          | `eval('2+3')`                        | 5                            |
| `exec()`         | Executes Python code                   | `exec('x=5')`                        | —                            |
| `filter()`       | Filters elements using function        | `list(filter(lambda x:x>2,[1,2,3]))` | [3]                          |
| `float()`        | Converts a value to float              | `float(5)`                           | 5.0                          |
| `format()`       | Formats a value                        | `format(10,'b')`                     | '1010'                       |
| `frozenset()`    | Creates an immutable set               | `frozenset([1,2])`                   | frozenset({1,2})             |
| `getattr()`      | Returns value of an attribute          | `getattr(obj,'x')`                   | value                        |
| `globals()`      | Returns global symbol dictionary       | `globals()`                          | dict of global variables     |
| `hasattr()`      | Checks if object has attribute         | `hasattr(obj,'x')`                   | True/False                   |
| `hash()`         | Returns hash value                     | `hash("a")`                          | int hash value               |
| `help()`         | Displays help for object               | `help(len)`                          | Help text                    |
| `hex()`          | Converts integer to hexadecimal        | `hex(10)`                            | '0xa'                        |
| `id()`           | Returns memory address                 | `id(5)`                              | unique integer               |
| `input()`        | Reads input from user                  | `input("Enter: ")`                   | (user input)                 |
| `int()`          | Converts to integer                    | `int("10")`                          | 10                           |
| `isinstance()`   | Checks object type                     | `isinstance(5,int)`                  | True                         |
| `issubclass()`   | Checks class inheritance               | `issubclass(bool,int)`               | True                         |
| `iter()`         | Returns an iterator                    | `iter([1,2])`                        | iterator object              |
| `len()`          | Returns length                         | `len([1,2,3])`                       | 3                            |
| `list()`         | Converts to list                       | `list((1,2))`                        | [1,2]                        |
| `locals()`       | Returns local symbol dictionary        | `locals()`                           | dict of local variables      |
| `map()`          | Applies function to iterable           | `list(map(lambda x:x*2,[1,2]))`      | [2,4]                        |
| `max()`          | Returns maximum value                  | `max(1,5,3)`                         | 5                            |
| `memoryview()`   | Returns memory view object             | `memoryview(b'abc')`                 | <memory at …>                |
| `min()`          | Returns minimum value                  | `min(1,5,3)`                         | 1                            |
| `next()`         | Returns next item from iterator        | `next(iter([1,2]))`                  | 1                            |
| `object()`       | Base object                            | `object()`                           | object instance              |
| `oct()`          | Converts integer to octal              | `oct(10)`                            | '0o12'                       |
| `open()`         | Opens a file                           | `open('file.txt','w')`               | file object                  |
| `ord()`          | Returns ASCII/Unicode code             | `ord('A')`                           | 65                           |
| `pow()`          | Returns x raised to y                  | `pow(2,3)`                           | 8                            |
| `print()`        | Displays output                        | `print("Hi")`                        | Hi                           |
| `property()`     | Creates a property in class            | Used in class                        | —                            |
| `range()`        | Generates sequence of numbers          | `list(range(3))`                     | [0,1,2]                      |
| `repr()`         | Returns string representation          | `repr("hi")`                         | "'hi'"                       |
| `reversed()`     | Reverses sequence                      | `list(reversed([1,2]))`              | [2,1]                        |
| `round()`        | Rounds a number                        | `round(3.6)`                         | 4                            |
| `set()`          | Creates a set                          | `set([1,1,2])`                       | {1,2}                        |
| `setattr()`      | Sets attribute of object               | `setattr(obj,'x',10)`                | —                            |
| `slice()`        | Returns slice object                   | `slice(1,5)`                         | slice(1,5,None)              |
| `sorted()`       | Returns sorted list                    | `sorted([3,1,2])`                    | [1,2,3]                      |
| `staticmethod()` | Creates static method in class         | Used in class                        | —                            |
| `str()`          | Converts to string                     | `str(10)`                            | "10"                         |
| `sum()`          | Returns sum of elements                | `sum([1,2,3])`                       | 6                            |
| `super()`        | Returns parent class object            | Used in class                        | —                            |
| `tuple()`        | Converts to tuple                      | `tuple([1,2])`                       | (1,2)                        |
| `type()`         | Returns type of object                 | `type(5)`                            | <class 'int'>                |
| `vars()`         | Returns **dict** of object             | `vars()`                             | dict of object attributes    |
| `zip()`          | Combines iterables                     | `list(zip([1,2],[3,4]))`             | [(1,3),(2,4)]                |
| `__import__()`   | Imports a module                       | `__import__('math')`                 | <module 'math'>              |
```

```python
#  --> Commonly used Built-in functions with Examples

'''

| Function   | Description                 | Example                                   | Output          |
| ---------- | --------------------------- | ----------------------------------------- | --------------- |
| `print()`  | Displays output             | `print("Hello")`                          | Hello           |
| `input()`  | Takes user input            | `input("Enter: ")`                        | (user input)    |
| `len()`    | Returns length              | `len("Python")`                           | 6               |
| `type()`   | Returns data type           | `type(10)`                                | `<class 'int'>` |
| `int()`    | Converts to integer         | `int("5")`                                | 5               |
| `float()`  | Converts to float           | `float("3.2")`                            | 3.2             |
| `str()`    | Converts to string          | `str(100)`                                | "100"           |
| `sum()`    | Adds elements               | `sum([1,2,3])`                            | 6               |
| `max()`    | Largest value               | `max(4,9,2)`                              | 9               |
| `min()`    | Smallest value              | `min(4,9,2)`                              | 2               |
| `abs()`    | Absolute value              | `abs(-7)`                                 | 7               |
| `round()`  | Rounds number               | `round(3.6)`                              | 4               |
| `range()`  | Generates sequence          | `list(range(1,5))`                        | [1,2,3,4]       |
| `sorted()` | Sorts elements              | `sorted([3,1,2])`                         | [1,2,3]         |
| `ord()`    | Character → ASCII           | `ord('A')`                                | 65              |
| `chr()`    | ASCII → Character           | `chr(65)`                                 | 'A'             |
| `bin()`    | Decimal → Binary            | `bin(10)`                                 | '0b1010'        |
| `id()`     | Returns memory address      | `id(5)`                                   | (unique number) |
| `format()` | Formats value               | `format(10,'b')`                          | '1010'          |
| `map()`    | Apply function to all items | `list(map(lambda x:x*2,[1,2,3]))`         | [2,4,6]         |
| `filter()` | Filter elements             | `list(filter(lambda x:x%2==0,[1,2,3,4]))` | [2,4]           |
| `zip()`    | Combine iterables           | `list(zip([1,2],[3,4]))`                  | [(1,3),(2,4)]   |
                                                                                                                     '''


# Most commonly used built-in function in python

'''
Most important functions to remember:

Input/Output → print(), input()
Type conversion → int(), float(), str()
Data handling → len(), sum(), max(), min()
Special → ord(), chr(), bin()
Advanced → map(), filter(), zip()   

'''
```

```python
#1. print()

# Description: Displays output to the console.

print("Hello, Python!")
```

```python
#2. input()

# Description: Reads input from the user.

name = input("Enter your name: ")
print("Hello,", name)
```

```python
# inner function works first (input()) then outer function works (int())
# input funput Always accept the values by default in string

a=int(input("Enter the A value: "))  
b=int(input("Enter the B value: "))
c=a+b
print("The value of sum",c)
```

```python
# 3. len()

# Description: Returns the length of a string, list, tuple, etc.

print(len("Python"))
print(len([1,2,3,4]))
```

```python
# 4. type()

# Description: Returns the type of a variable or object.

print(type(5))
print(type("Hello"))
```

```python
# 5. int()

# Description: Converts a value to an integer.


num = int("10")
print(num + 5)
```

```python
# 6. float()

# Description: Converts a value to a floating-point number.

num = float("3.14")
print(num + 1)
```

```python
# 7. str()

# Description: Converts a value to a string.


num = 10
print("Number: " + str(num))
```

```python
# 8. sum()

# Description: Returns the sum of elements in a list or iterable.

numbers = [1, 2, 3, 4]
print(sum(numbers))
```

```python
# 9. max()

# Description: Returns the maximum value in a list or among arguments.

print(max(5, 10, 3))
print(max([2, 7, 1]))
```

```python
# max() used in string and it returns a maximum value by alphabet order 

a=["Java","Python","C++","Html"]
a = max(a)
a
```

```python
# 10. min()

# Description: Returns the minimum value in a list or among arguments.

print(min(5, 10, 3))
print(min([2, 7, 1]))
```

```python
# in alphabetic order the list starting element index contains duplicates "Z"so it takes second element "e"

a=["Zebra","zudio","zomato"]
a = min(a) 
a
```

```python
# 11. abs()

# Description: Returns the absolute value of a number.

print(abs(-7))
```

```python
# 12. round()

# Description: Rounds a floating-point number to the nearest integer.

print(round(3.6))
print(round(3.2))
```

```python
# 13. range()

# Description: Generates a sequence of numbers.

for i in range(1, 5):
    print(i)
```

```python
# 14. sorted()

# Description: Returns a sorted list from an iterable.

numbers = [3, 1, 2]
print(sorted(numbers))
```

```python
# descending order sorted

numbers = [4,1,3,2]
print(sorted(numbers,reverse=True))
```

```python
# 15. ord()

# Description: Returns the ASCII/Unicode code of a character.

print(ord('A'))
```

```python
# 16. chr()

# Description: Returns the character corresponding to an ASCII/Unicode code.

print(chr(65))
```

```python
# 17. bin()

# Description: Converts an integer to binary string.

print(bin(10))
```

```python
# 18. id()

# Description: Returns the memory address of an object.

x = 5
print(id(x))
```

```python
# 19. format()

# Description: Formats a value in a specific format.

print(format(10, 'b'))  # binary
print(format(255, 'x')) # hexadecimal
```

```python
# 20. map()

# Description: Applies a function to each item in an iterable.

nums = [1, 2, 3]
result = list(map(lambda x: x*2, nums))
print(result)
```

```python
# 21. filter()

# Description: Filters elements based on a function.

nums = [1, 2, 3, 4]
result = list(filter(lambda x: x%2==0, nums))
print(result)
```

```python
# 22. zip()

# Description: Combines multiple iterables into tuples.

a = [1,2]
b = ['x','y']
print(list(zip(a,b)))
```

```python
# Functions using modules

'''

| Library    | Function       | Description         | Example                |
| ---------- | -------------- | ------------------- | ---------------------- |
| `math`     | `sqrt(x)`      | Returns square root | `math.sqrt(16) → 4`    |
| `math`     | `ceil(x)`      | Rounds up           | `math.ceil(4.2) → 5`   |
| `math`     | `floor(x)`     | Rounds down         | `math.floor(4.8) → 4`  |
| `random`   | `random()`     | Random number (0–1) | `random.random()`      |
| `random`   | `randint(a,b)` | Random integer      | `random.randint(1,10)` |
| `datetime` | `date.today()` | Current date        | `date.today()`         |
| `os`       | `getcwd()`     | Current directory   | `os.getcwd()`          |
| `sys`      | `exit()`       | Exit program        | `sys.exit()`           |                        '''
```

```python
# Mathematical Functions in Python (math module)
# Import math module before using

'''

| Function          | Description       | Example              | Output |
| ----------------- | ----------------- | -------------------- | ------ |
| `math.sqrt(x)`    | Square root       | `math.sqrt(16)`      | 4.0    |
| `math.ceil(x)`    | Round up          | `math.ceil(4.2)`     | 5      |
| `math.floor(x)`   | Round down        | `math.floor(4.8)`    | 4      |
| `math.pow(x,y)`   | Power             | `math.pow(2,3)`      | 8.0    |
| `math.fabs(x)`    | Absolute value    | `math.fabs(-5)`      | 5.0    |
| `math.log(x)`     | Natural log       | `math.log(10)`       | 2.30   |
| `math.log10(x)`   | Log base 10       | `math.log10(100)`    | 2.0    |
| `math.exp(x)`     | e^x               | `math.exp(2)`        | 7.38   |
| `math.sin(x)`     | Sine              | `math.sin(0)`        | 0.0    |
| `math.cos(x)`     | Cosine            | `math.cos(0)`        | 1.0    |
| `math.tan(x)`     | Tangent           | `math.tan(45)`       | 1.61   |
| `math.degrees(x)` | Radians → Degrees | `math.degrees(3.14)` | 179.9  |
| `math.radians(x)` | Degrees → Radians | `math.radians(180)`  | 3.14   |
```
