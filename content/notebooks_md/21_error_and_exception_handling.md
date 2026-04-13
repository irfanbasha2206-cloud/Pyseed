# 21 - Error and Exception Handling

```python
# There are three main categories of errors

'''
--> Syntax errors (compile-time)
--> Runtime errors (exceptions)
--> Logical errors

'''

# 1. Compile-Time Error (Syntax Error in Python)
'''
Python doesn’t have a separate “compile phase” like some languages, but it checks syntax before running. So compile-time errors are usually called syntax errors.

--> Happens before execution
--> Code won’t run at all
--> Python shows an error immediately

Example:
'''
if x > 5
    print(x)


# 2. Runtime Error
'''
--> Happens while the program is running
--> Program crashes unless handled
--> Shows an exception
Example:
'''
x = 10 / 0           # ZeroDivisionError

 
# 3. Logical Error
'''
Program runs successfully
But gives wrong output
No error message

Example:
'''
a = 10
b = 20
print(a + b / 2)   # Wrong logic
                   # Python follows BODMAS/PEMDAS, so division happens before addition 
# corrected code

a = 10
b = 20
print((a + b) / 2) # Whenever you write formulas, use parentheses to control calculation order
```

```python
# Difference between Error handlind and Exception Handling

'''

| Feature    | Error Handling                     | Exception Handling                         |
| ---------- | ---------------------------------- | ------------------------------------------ |
| Definition | General process of managing errors | Handling runtime errors using `try-except` |
| Approach   | Prevent errors before they occur   | Handle errors after they occur             |
| Technique  | Conditions, validations            | `try`, `except`, `finally`, `else`         |
| Type       | Broad concept                      | Part of error handling                     |
| Example    | Checking `y != 0` before division  | Using `try-except` block                   |



Error Handling → Prevent errors (before execution)
Error handling is the overall concept of managing errors.

Exception Handling → Handle errors (during execution)   
Exception handling is a specific way to handle runtime errors using Python’s built-in mechanisms.    '''
```

```python
# Built-in Exceptions
'''

--> General / Base Errors
Exception → Base class for most errors
BaseException → Root of all exceptions (rarely used directly)

--> Syntax & Parsing Errors
SyntaxError → Invalid Python syntax
IndentationError → Wrong indentation
TabError → Mixing tabs and spaces

--> Name & Type Errors
NameError → Variable not defined
UnboundLocalError → Local variable used before assignment
TypeError → Wrong type used

--> Value & Attribute Errors
ValueError → Right type, wrong value
AttributeError → Attribute/method doesn’t exist

--> Indexing & Key Errors
IndexError → List index out of range
KeyError → Dictionary key not found

--> File & I/O Errors
FileNotFoundError → File doesn’t exist
PermissionError → No permission to access file
IsADirectoryError → Expected file but got directory
NotADirectoryError → Expected directory but got file
IOError → General I/O error (merged into OSError in Python 3)

--> Arithmetic Errors
ZeroDivisionError → Division by zero
OverflowError → Number too large
FloatingPointError → Floating point failure

--> Import Errors
ImportError → Import failed
ModuleNotFoundError → Module not found

--> Runtime Errors
RuntimeError → Generic runtime failure
RecursionError → Maximum recursion exceeded
NotImplementedError → Feature not implemented

--> OS / System Errors
OSError → OS-related issues
TimeoutError → Operation timed out
ConnectionError → Base for network errors
ConnectionRefusedError
ConnectionResetError
ConnectionAbortedError

--> Assertion & Debugging
AssertionError → assert statement failed

--> Stop / Control Flow
StopIteration → End of iterator
StopAsyncIteration → End of async iterator

--> Memory Errors
MemoryError → Out of memory

--> Keyboard / System Exit
KeyboardInterrupt → User pressed Ctrl+C
SystemExit → Program exit                                            '''
```

```python
# 1. Error Handling in Python

'''
Definition:-

Error handling is the process of identifying and managing errors in a program so that it does not crash and can run smoothly.

It is a general concept.
Includes checking conditions and preventing errors before they occur. 

'''

# Example (Error Handling using condition)

x = 10
y = 0

if y != 0:
    print(x / y)
else:
    print("Cannot divide by zero")   # Here, we prevent the error using a condition.
```

```python
num = input("Enter a number: ")

if num.isdigit():   # checking before execution
    print(int(num) + 10)
else:
    print("Invalid input!")
```

```python
# 2. Exception Handling in Python (Run time error)

'''
Definition:-

It is a specific technique used in error handling .Handles errors after they occur.

Exception handling is a method of handling runtime errors (exceptions) using special Python keywords like 

try 
except 
else
finally

'''
```

```python
'''
try
--> Code that might cause an error goes here. 
'''

try:
    x = int("abc")   # risky code

'''
except
--> Runs if an error occurs in try.
'''

except ValueError:               # Specific the Exception
    print("Cannot convert to integer")

'''
else
--> Runs only if NO exception occurs.
'''

else:
    print("Conversion successful:", x)

'''
finally
--> Runs no matter what (error or no error).
--> Used for cleanup (closing files, releasing resources).
'''

finally:
    print("This always runs")
```

```python
# Alltogether
# zero error execution

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
```

```python
# tried with zero

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
```

```python
# tried with invalid number

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
```

```python
# most common handled errors :
'''
NameError
ValueError
TypeError
KeyError
IndexError
FileNotFoundError
AttributeError
ZeroDivisionError
ImportError 
ModuleNotFoundError     

'''
```

```python
# Explanation each most common error with examples

# 1. ValueError
# Occurs when the value is invalid.


try:
    num = int(input("Enter The Number"))
    print(num * 100)
except ValueError:
    print("Invalid Input..! Please Enter a Number for operations")
```

```python
# 2. ZeroDivisionError
# Occurs when dividing by zero.

try:
    x = 10
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

```python
# 3. IndexError
# Occurs when accessing invalid index.

try:
    a = [10,20,30,40]
    print(a[5])
except IndexError:
    print("Index Out of Range")
```

```python
# 4. KeyError
# Occurs when dictionary key not found.

try:
    data = {"Name": "Irfan","Age": 21}
    print(data["city"])
except KeyError:
    print("Key is not found in Dictionary")
```

```python
# 5. FileNotFoundError
# occurs when Python cannot locate the file you are trying to open or access.


try:
    file = open(r"user\python\py1.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
```

```python
# 6. TypeError
# Occurs when incompatible data types are used.

try:
    print("10" + 5)
except TypeError:
    print("Type mismatch error")
```

```python
# 7. NameError
# Occurs when variable is not defined.

try:
    a = 20
    print(b)
except NameError:
    print("Name is not defined")
```

```python
# 8. AttributeError
#Occurs when you try to use an attribute (method/property) that does not exist for an object.

try:
    x = 10
    x.append(5)   # invalid for integer
except AttributeError:
    print("Attribute does not exist")
```

```python
# 9.ImportError 
# Occurs when Python cannot find the module

try:
    import abcxyz
except ModuleNotFoundError:
    print("Module not found")
```

```python
# 10. ModuleNotFoundError
# Occurs when the module exists but something inside it cannot be imported

try:
    from math import abc
except ImportError:
    print("Cannot import name")
```

```python
# Exception keyword
# Exception is the parent class of most built-in errors
# Using except Exception: allows you to handle all errors generically, instead of specifying each one.

# display error as it shows by handling ZeroDivisionError

try:
    a = 10
    b = 0 
    c = a / b
    print(c)
except Exception as e:
    print(e)
```

```python
# display error as it shows by handling ValueError

try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = a + b
    print(c)
except Exception as e:
    print(e)
```

```python
# display error by user friendly statements by handling ZeroDivisionError

try:
    a = 10
    b = 0 
    c = a / b
    print(C)
except Exception:
    print("OOPS..! Something Went Wrong")
```

```python
# display error by user friendly statements by handling NameError

try:
    a = "Irfan"
    b = "Basha"
    print(a+b+c)
except Exception as e:
    print("OOPS..! Something Went Wrong")
```

```python
# display error by user friendly statements by handling FileNotFoundError

try:
    file = open(r"user\python\py1.txt","r")
    print(file.read())
except Exception:
    print("File Not Found")
```
