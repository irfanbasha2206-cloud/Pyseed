# 1 -  Variables and Datatypes

```python
print("hello world")
```

```python
print("hello" , "Irfan" , end=" ")
print("java")
print("python") #every print fucntion has inbuild (end="\n")
```

```python
print("hello\nworld") #\n is used to line break or seperate line in strings
```

```python
print("hello\tworld") #\t is used for 1 tab space or 4 comman spaces
```

```python
# 1. Variable

'''
  A variable is a name that refers to a value stored in memory.

 It is like a container that holds data which can be used and manipulated throughout the program.

Key points:

Variables store values of different data types.
The value of a variable can change anytime.
Python does not require declaring the type of a variable explicitly (dynamic typing)    '''
```

```python
a=5                     # here a is variable and 5 is data
print(a)
```

```python
name = "irfan"
print("name") #when variable was assinged to a value then it not called in double qoutes
```

```python
a=5
b=10
c=a+b
print(c)
```

```python
a=10
a=100
a=1000
print(a) #the last updated value would be stores everytime in that variable name
```

```python
a=10
a=a+100
print(a)
```

```python
#Bodmas rule => bracket , order , division ,multiplication ,addition ,subtraction
c=32                             #2+5/2 => 4.5 , (2+5)/2 =>3.5
f=(c*9/5)+32
print(f)
```

```python
#area of a rectangle
l=34
w=40
a=l*w
print(a)
```

```python
#volume of a sphere
r=3
pie=3.14
v=4/3*pie*r**3
print(v)
```

```python
# 2. Data Type

'''

A data type defines the type of a single variable — i.e., what kind of value it can hold.
It tells Python how to interpret the value.


Examples of data types:

Numeric: int, float, complex
Text: str
Boolean: bool
Binary: bytes, bytearray
Sequence: list, tuple, range
Set: set, frozenset
Mapping: dict    

--> Python has several built-in data types, broadly categorized into:


| Category | Data Type                    | Example                        |
| -------- | ---------------------------- | ------------------------------ |
| Numeric  | int, float, complex          | `x=5, y=3.14, z=2+3j`          |
| Sequence | list, tuple, range           | `[1,2,3], (1,2,3), range(1,5)` |
| Text     | str                          | `"Hello"`                      |
| Set      | set, frozenset               | `{1,2,3}, frozenset([1,2])`    |
| Mapping  | dict                         | `{'name':'Alice'}`             |
| Boolean  | bool                         | `True, False`                  |
| Binary   | bytes, bytearray, memoryview | `b'Hi', bytearray([65,66])`    |               '''
```

```python
'''
1. Numeric Data Types

Used to store numbers.

Type	      Description	        Example
int	         Integer numbers	    x = 10
float	     Decimal numbers	    y = 3.14
complex	     Complex numbers	    z = 2 + 3j   '''

x = 10       # int
y = 3.14     # float
z = 2 + 3j   # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```

```python
'''
2. Sequence Data Types

Used to store multiple items in order.

Type	Description	                     Example
list	 Ordered,                  mutable collection [1, 2, 3]
tuple	 Ordered,                  immutable collection	(1, 2, 3)
range	 Sequence of numbers	      range(1, 5)                   '''

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_range = range(1, 5)

print(type(my_list))   # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>
print(type(my_range))  # <class 'range'>
```

```python
'''
3. Text Type

Used to store textual data.

Type	Description	Example
str	String (sequence of characters)	"Hello"

Example: '''

name = "Python"
print(type(name))  # <class 'str'>
```

```python
'''
4. Set Data Types

Used to store unique, unordered elements.

Type	       Description	                           Example
set	           Mutable collection of unique items	   {1, 2, 3}
frozenset	   Immutable set	                       frozenset([1,2,3])   '''

my_set = {1, 2, 3, 2}
print(my_set)        # {1, 2, 3} (duplicates removed)
print(type(my_set))  # <class 'set'>
```

```python
'''
5. Mapping Data Type

Used to store key-value pairs.

Type	  Description	      Example
dict	  Dictionary	     {'name': 'Alice', 'age': 25}      '''

person = {'name': 'Alice', 'age': 25}
print(type(person))       # <class 'dict'>
print(person['name'])     # Alice
```

```python
'''
6. Boolean Type

Stores True or False values.

Type	  Description     	  Example
bool	   Boolean	        True or False

Example:                               '''

x = True
y = False
print(type(x))  # <class 'bool'>
```

```python
'''
7. Binary Data Types

Used to store binary data.

Type	          Description	                     Example
bytes	       Immutable sequence of bytes  	      b"Hello"
bytearray	    Mutable sequence of bytes	         bytearray([65,66])
memoryview	    Memory view object	                 memoryview(b"abc")    '''


b = b"Hello"
ba = bytearray([65,66])
mv = memoryview(b"abc")

print(type(b))   # <class 'bytes'>
print(type(ba))  # <class 'bytearray'>
print(type(mv))  # <class 'memoryview'>
```

```python
'''
commonly used 4 types of datatypes:

str--> any characters like words , numbers and symbols that represents in double or single quotes ("hello" or '123')
int--> represents in numerical characters or interger (1,2,3,4,.....)
float--> represents in decimal or point values (1.0 , 1.1 , 1.2 , 1.3 , 1.4,....)
boolean--> it is oftenly used in operator calculations like comparison , logical , membership and identity which represents in true or false'''
```

```python
#str datatype
a="dead end"      #here the word (dead end) stored in the variable under the double quotes "" which represents a string
print(a)
```

```python
#int datatype
a=50            #here the number (50) is stored in the variable which represent a integer
print(a)
```

```python
#float datatype 
a=1.20            #here the decimal value (1.20) is stored in the variable which represents a float
print(a)
```

```python
#boolean datatype
a=5>3           #here the comparison operator greater than (>) is used to compare two values which gives output of true and it is an boolean
print(a)
```
