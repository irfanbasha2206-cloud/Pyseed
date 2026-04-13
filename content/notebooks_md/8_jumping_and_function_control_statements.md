# 8 - Jumping and Function Control Statements

```python
# Jumping Statements 

'''
Jumping statements are used to change the normal flow of execution in a program, especially inside loops.

They can:

--> Stop a loop
--> Skip an iteration
--> Do nothing (placeholder)

'''

# Types of Jumping Statements

'''
 -->break
 -->continue
 -->pass
 
 '''
```

| Statement  | Where it works | Effect                                    |
| ---------- | -------------- | ----------------------------------------- |
| `break`    | Loops          | Stops the loop completely                 |
| `continue` | Loops          | Skips current iteration                   |
| `pass`     | Any block      | Does nothing (placeholder)                |

```python
# break 

'''
 break is used only in looping to terminate the loop before when they finish naturally
 Useful when you want to stop processing once a condition is met
'''

for i in range(5):
    if i==3:
        break      
    else:
        print(i)
```

```python
for i in range(5):
    if i==3:
        print(i)
        break
```

```python
for i in range(4):
    print("Hello")
    break
    print("python")
```

```python
# continue

'''
# Used to skip the current iteration of a loop.
#The loop does not end, it just moves to the next iteration.
'''

for i in range(4):
    if i == 2:
        continue       #here i satisfied by 2 and skip the 2nd iteration
    print(i)
    print("Hello")
```

```python
for i in range(3):
    if i==1:
        continue
        print(i)
        print("Hello")
    print("Java")
```

```python
for i in range(3):
    if i==1:
        print(i)
        continue
        print("Hello")
    print("Java")
```

```python
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("loop completed")
```

```python
# pass

'''
# pass is used as a placeholder when no action is needed
# Helps avoid syntax errors when a block cannot be empty.
# pass is temporarily statement used inside the if statements , loops , functions and classes and to  add the logic later.
# Python does not allow empty blocks. If you leave a function, loop, or condition empty, it will give an error. So, you use pass to avoid that.
'''

# pass used in if condition
x = 10

if x > 5:
    pass
    
print(x)
```

```python
#pass in loop
for i in range(5):
    pass                 # Loop runs, but no action is performed.
```

```python
for i in range(3):
    pass

print("Loop completed")  # Loop executes, but nothing happens inside it.
```

```python
# pass in function
def my_function():
    pass
my_function()
```

```python
#pass in class
class Student:
    pass

s = Student()
```

```python
# Function Control Statements in Python

'''
Function control statements determine how a function behaves when it runs.
They can stop function execution, return values, or pause execution (in case of generators).
'''

# Main Function Control Statements


'''
--> return
--> yield
--> raise (used to throw exceptions, can stop function execution)
```

| Statement | Purpose                                 | Effect                                     |
| --------- | --------------------------------------- | ------------------------------------------ |
| `return`  | Stop function & optionally return value | Exits function immediately                 |
| `yield`   | Pause function & return generator value | Allows function to resume later            |
| `raise`   | Raise exception                         | Stops function unless exception is handled |

```python
# return

'''
# return statement is used inside a function to send a result back to wherever the function was called.
# Used inside functions to exit immediately and optionally return a value and stored into the current function name.
# Any code after return in the function will not run.
'''


#example of using return in def function
def add(a,b):
    return a+b      # here it returns and stored in the add function name
    
val1=add(5,5)    # here we assigning a new variable to the add 
print(val1)
```

```python
#example of using print in def function
def add(a,b):
    print(a+b)
    
result=add(5,5)
print(result)    #with print statement used inside the def function it not hold that add function so using new variable to add and it prints none
```

```python
#example of using return in def function
def add(a, b):
    return a + b    #with return statement used inside the functions it returns the value to def parameters with print function

result = add(2, 3)
print(result)
```

```python
def greet(name):
    print("Hello", name)  #here return is not used so the outer print funtion results in none

result = greet("John")
print(result)
```

```python
# Returning Multiple Values
def get_values():
    return 1, 2, 3

a, b, c = get_values()
print(a, b, c)
```

```python
def check(n):
    if n > 150:
        return "Large"
    elif n > 100 and n <= 150:
        return "medium"
    else:
        return "small"
    print("hello")             # here we code if family statements and individual print statements also. when the condition is satisfied return statement 
    print("world")               # returns it value and terminate its entire function because it is jumping statement.

check(170)
```

```python
def check(n):
    if n > 150:
        print("Large")
    elif n > 100 and n <= 150:
        print("medium")
    else:
        print("small")
    print("hello")            # here we use print instead of return in if family so the individual print sataements also prints
    print("world")              

check(170)
```

```python
# yield

'''
Used in generator functions.
Pauses the function and returns a value, but keeps the function state.
Allows the function to resume later.

Example:
'''

def numbers():
    for i in range(3):
        yield i

for num in numbers():
    print(num)
```

```python
# raise

'''
Used to raise an exception inside a function.
Immediately stops function execution unless handled by try-except.

Example:
'''

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(divide(10, 2))
```
