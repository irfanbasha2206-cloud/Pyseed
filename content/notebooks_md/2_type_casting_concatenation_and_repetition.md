# 2  - Type Casting , Concatenation and Repetition

```python
# Type conversion or type casting is called changing or convert one datatype to another datatype

'''
Type casting in Python refers to converting a value from one data type to another. 
It is useful when you need to perform operations that require compatible data types.

Type casting and type conversion are often used interchangeably, but there is a small theoretical difference

Type Conversion → General term (includes both automatic and explicit (manual conversion))
Type Casting → Usually refers to manual (explicit) conversion

Types of Type Casting

--> Implicit casting: Done automatically by Python (Automatic)
--> Explicit casting: Done manually using functions (Manual)

Why Type Casting is Needed
To perform mathematical operations
To process user input (input is always string)
To ensure compatibility between different data types
To control data format in programs

'''
```

```python
# Explicit Type Casting (Manual)

'''
The programmer manually converts data types using built-in functions.

Common Explicit Type Casting using Buit-in Functions 

Function	Description
int()	 Converts to integer
float()	 Converts to float
str()	 Converts to string
bool()	 Converts to boolean
list()	 Converts to list
tuple()	 Converts to tuple
set()	 Converts to set  

'''

my_name = "Irfan"
my_age = 25
my_gpa = 3.7
my_student = (True) or (False)
my_list = [1,1,2,2,3,3,4,4]
my_tuple =(1,2,3,4,5)
my_set = {5,2,1,3,4}

print(type(my_name))
print(type(my_age))
print(type(my_gpa))
print(type(my_student))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
```

```python
# string to integer type cast

char = "90"
char_2 = int(char)
print(char)
print(type(char))
print(char_2)
print(type(char_2))
```

```python
# integer to string type cast

cooky = 66
cooky_2 = str(cooky)
print(cooky)
print(type(cooky))
print(cooky_2)
print(type(cooky_2))
```

```python
# Not all conversions are possible:
# Error (invalid literal)

hello = "hello"
hello_2 = int(hello)
print(hello_2)
```

```python
# string to boolean type cast
# Boolean data type displays either true or false when assigned to a variable in an empty str that would be false

empty = ""
empty_2 = bool(empty)
print(empty)
print(type(empty))
print(empty_2)
print(type(empty_2))
```

```python
# boolean to string type cast

condition = True
condition_2 = str(condition)
print(condition)
print(type(condition))
print(condition_2)
print(type(condition_2))
```

```python
# integer to boolean type cast
# In python any nummber but 0 is considered False

mark = 0                  
mark_2 = bool(mark)
print(mark)
print(type(mark))
print(mark_2)
print(type(mark_2))
```

```python
# integer to float type cast

love = 5                      
love_2 = float(love) 
print(love)
print(type(love))
print(love_2)
print(type(love_2))
```

```python
# integer to boolean type cast
# when coverting a integer to a boolean if that number anything but zero it always be true

age = 25                       
age_2 = bool(age) 
print(age)
print(type(age))
print(age_2)   
print(type(age_2))
```

```python
# list to tuple type cast

list_1 = [1,2,3,4]
list_2 = tuple(list_1)
print(list_1)
print(type(list_1))
print(list_2)
print(type(list_2))
```

```python
# list to set type cast

list_1 = [1,2,3,4]
list_2 = set(list_1)
print(list_1)
print(type(list_1))
print(list_2)
print(type(list_2))
```

```python
# Tuple to set type cast

t1 = (1,2,3,4,5,5,5)
set_1 = set(list_1)        # by converting to set it removes duplicate values
print(t1)
print(type(t1))
print(set_1)
print(type(set_1))
```

```python
# set to list type cast
set_1 = {1,2,3,4,5,6,6,6}
list_1 = list(set_1)
print(set_1)
print(type(set_1))
print(list_1)
print(type(list_1))
```

```python
# Implicit Type Casting (Automatic)

'''
Python automatically converts one data type to another when it is safe to do so (usually from smaller to larger types).
A variable datatype can be converted when you perform certain arrithmetic operations like division
example:-
'''

a = 5       # int
b = 2.5     # float

c = a + b   # int is converted to float automatically
print(c)    # 7.5
print(type(c))  # float
```

```python
# Concatenation
# Joining two sequences together using +

'''
Data Types That Support Concatenation

a) Strings (str) ---> joins two strings
b) Lists (list)  ---> joins two lists
c) Tuples (tuple) ---> joins two tuples
d) Bytes (bytes)  ---> joins byte sequences
e) Bytearray (bytearray) ---> joins bytearrays   '''
```

```python
# String Concatenation 
# using alphabetic characters in String Concatenation 
a = "Hello"
b = "World"
print(a + " " + b)
```

```python
# using integers in String Concatenation 
# Concatenate string + integer leads to error
a = "5"
b = "5"
print(a + b)
```

```python
# List Concatenation

list1 = [1,2]
list2 = [3,4]
print(list1 + list2)
```

```python
# Tuple Concatenation

t1 = (1,2)
t2 = (3,4)
print(t1 + t2)
```

```python
# Byte Concatenation

b1 = b'abc'
b2 = b'def'

print(b1 + b2)
```

```python
# Bytearray Concatenation

ba1 = bytearray(b'12')
ba2 = bytearray(b'34')

print(ba1 + ba2)
```

```python
# Repetition
# Repeating a sequence multiple times using *

'''
Data Types That Support Repetition

a) Strings (str) ---> repeats the strings
b) Lists (list)  ---> repeats two lists
c) Tuples (tuple) ---> repeats two tuples
d) Bytes (bytes)  ---> repeats byte sequences
e) Bytearray (bytearray) ---> repeats bytearrays   '''
```

```python
# string Repetition 
# it repeats the string by arithmetic operator "*" into given number of times

a = "irfan " 
print(a* 3)
```

```python
# List Repetition


list1 = [1,2]
list2 = [3,4]

print(list1 * 3)      
print(list2 * 3)
```

```python
# Tuple Repetition

t1 = (1,2)
t2 = (3,4)

print(t1 * 3)
print(t2 * 3)
```

```python
# Byte Repetition

b1 = b'abc'
b2 = b'def'

print(b1 * 3)
```

```python
# Bytearray Repetition

ba1 = bytearray(b'12')
ba2 = bytearray(b'34')

print(ba1 * 3)
```
