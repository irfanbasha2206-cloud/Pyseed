# 3  - Operators

```python
# Operators 

'''
Operators are special symbols or keywords in Python that perform operations on values (operands).
They are used for mathematical calculations, comparisons, logical operations, and more.

They help the program compute, compare, or control flow
'''

# Types of Operators

'''
```

```python
# Mathematical operators

'''
1 Arithmetic operators 

Purpose: Perform mathematical calculations.
Operators: + - * / // % **

Example Table:

| Operator | Meaning             | Example  | Output |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | 8      |
| `-`      | Subtraction         | `5 - 3`  | 2      |
| `*`      | Multiplication      | `5 * 3`  | 15     |
| `/`      | Division (float)    | `5 / 2`  | 2.5    |
| `//`     | Floor division      | `5 // 2` | 2      |
| `%`      | Modulus (remainder) | `5 % 2`  | 1      |
| `**`     | Exponentiation      | `2 ** 3` | 8      |
 
 '''

a=4
b=5
c=a**b
print(c)
```

```python
a=5
b=2
c=a/b
print(c)
```

```python
a=5
b=5
c=a%b
print(c)
```

```python
# Assingnment operators 

'''
Purpose: Assign values to variables, optionally modify them.
Operators: =, +=, -=, *=, /=, //=, %=, **=

Example Table: 

| Operator | Meaning                 | Example   | Equivalent To |
| -------- | ----------------------- | --------- | ------------- |
| `=`      | Assign value            | `x = 10`  | —             |
| `+=`     | Add and assign          | `x += 5`  | `x = x + 5`   |
| `-=`     | Subtract and assign     | `x -= 3`  | `x = x - 3`   |
| `*=`     | Multiply and assign     | `x *= 2`  | `x = x * 2`   |
| `/=`     | Divide and assign       | `x /= 4`  | `x = x / 4`   |
| `//=`    | Floor divide and assign | `x //= 3` | `x = x // 3`  |
| `%=`     | Modulus and assign      | `x %= 3`  | `x = x % 3`   |
| `**=`    | Exponent and assign     | `x **= 2` | `x = x ** 2`  |

'''

x=10
x+=5
print(x)
```

```python
y=10
y*=4
print(y)
```

```python
# Comparison operators

'''
Purpose: Compare two values. Returns True or False.
Operators: == != > < >= <=

Example Table:

| Operator | Meaning          | Example  | Output |
| -------- | ---------------- | -------- | ------ |
| `==`     | Equal to         | `5 == 3` | False  |
| `!=`     | Not equal to     | `5 != 3` | True   |
| `>`      | Greater than     | `5 > 3`  | True   |
| `<`      | Less than        | `5 < 3`  | False  |
| `>=`     | Greater or equal | `5 >= 5` | True   |
| `<=`     | Less or equal    | `5 <= 3` | False  |

'''

a = 5<2
print(a)
```

```python
5!=5
```

```python
5==5
```

```python
5>=4
```

```python
# logical operators 

'''
Purpose: Combine Boolean conditions.
Operators: and, or, not

Example Table:

| Operator | Meaning               | Example          | Output |
| -------- | --------------------- | ---------------- | ------ |
| `and`    | True if both True     | `True and False` | False  |
| `or`     | True if any True      | `True or False`  | True   |
| `not`    | Inverts boolean value | `not True`       | False  |

'''
```

```python
#and operator 
x=100
y=20
z=(x>y and x>y)     #if two conditions are satisfied the result will be in true
print(z)
```

```python
#or operator
x=30
y=35
z=(x==y or x<=y)     #if one condition satisfied the result will be in true
print(z)
```

```python
#not operator
x=20
y=25
z=not(x==y or x>=y)   #reverse the results (false= true)
print(z)
```

```python
4>2 or 7!=7 and 10<15      #() -> not -> and -> or -->conditions starts work from () to or operator if there is three or more conditions
                            # From this condition () & not is not there so it starts from and aperator
```

```python
# Membership operator 

'''
Purpose: Check if a value exists in a sequence (list, tuple, string).
Operators: in, not in

Example Table:

| Operator | Meaning                            | Example            | Output |
| -------- | ---------------------------------- | ------------------ | ------ |
| `in`     | True if value exists in a sequence | `3 in [1,2,3]`     | True   |
| `not in` | True if value does **not** exist   | `5 not in [1,2,3]` | True   |

'''
a="swim"
a="s" in "swim"
print(a)
```

```python
a="fool"
a="b" in "fool"
print(a)
```

```python
a="jockey"
a="m" not in "jockey"
print(a)
```

```python
a="metro"
a="m" not in "metro"
print(a)
```

```python
a="tamil"
a="T" in "tamil"     #Even if small "t" was present in that string when caps "T" was assinged to check in operator so it returns false
print(a)
```

```python
# Identity operator 

'''
| Operator | Meaning                                     | Example                        | Output |
| -------- | ------------------------------------------- | ------------------------------ | ------ |
| `is`     | True if both refer to **same object**       | `a = [1]; b = a; a is b`       | True   |
| `is not` | True if both refer to **different objects** | `a = [1]; b = [1]; a is not b` | True   |

'''
```

```python
a=10       
a=5        #two values are assinged in same variable name a and also it comes under -5 to 256 category series so it returns true
a is a
```

```python
a=300
b=300   #a is holding the same value of b and it come under >256 category series so it returns false 
a is b
```

```python
a=10
b=20   #two different values are assigned in different variables so it returns false
a is b
```

```python
a=10
b=10        # two same values are stored in different variable and also it comes under -5 to 256 category series so it returns true
a is b
```

```python
a=10
b=20        # a is not holding the same value of b it returns true by "is not" operator
a is not b
```

```python
a=10
a=20         # two values are assigned in same varable of a so it returns false by "is not" operator
a is not a
```

```python
# Alter Example of Identity operator 

'''
is -> to find the memory address in the ram 
is not -> to do not find the memory address in the ram
'''

a=10
b=100     # variable is a container that stores value by three categories variable name , datatype and id (14356778986)
id(a)     #(-5 to 256 - values are stored in same memory location even when it was assigned in same variable name)
id(b)     #(>256 - values are different memory location)
```

```python
a=90
a=10
id(a)
id(a)
```

```python
a=10
a=10
id(a)
id(b)
```

```python
# Bitwise operator 

'''
IT is not commonly used in Python
But you have to know about its top layer and but not go deep into it.

Purpose: Operate on binary representations of numbers.
Operators: & | ^ ~ << >>

Example Table:

| Operator | Meaning              | Example    | Binary Operation                     | Output |      
| -------- | -------------------- | ---------- | ------------------------------------ | ------ | 
| `&`      | Bitwise AND          | `5 & 3`    | 0101 & 0011 → 0001                   | 1      |               
| `|`      | Bitwise OR           | `5 | 3`    | 0101 | 0011 → 0111                   | 7      |
| `^`      | Bitwise XOR          | `5 ^ 3`    | 0101 ^ 0011 → 0110                   | 6      |                    
| `~`      | Bitwise NOT (invert) | `~5`       | ~0101 → 1010 (two’s complement → -6) | -6     |                    
| `<<`     | Left Shift           | `5 << 1`   | 0101 << 1 → 1010                     | 10     |                  
| `>>`     | Right Shift          | `5 >> 1`   | 0101 >> 1 → 0010                     | 2      |                    
  

'''
```

```python
5|3
```
