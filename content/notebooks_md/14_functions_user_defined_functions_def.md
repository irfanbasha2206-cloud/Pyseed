# 14 - Functions - User Defined functions (def)

```python
# Functions

'''
  functions are named blocks of code that are designed to do specific job.when you want to perform a particular task,
  you the name of the function responsible of it.if you need to perform that rask multiple times throughout your program 
  you don`t need to type all the code for the same task again and again; you just call the function dedicated to handling
  that task , and the calls tells python to run the code inside the function.                                                    '''

# Types of Functions
'''
--> User defined or def functions
--> Built-in functions
--> Lambda functions
--> Recursion functions                                                              '''
```

```python
#user defined function or def function

'''  A def function is how you define (create) your own reusable block of code. 
     It lets you create group of instructions of codes together and run them whenever needed by calling the function name.
     It is also called user defined function. 
     def function variable name are used widely whatever. '''

#example

def greet(name):
    print("Hello, " + name)

greet("irfan")
```

```python
def demo():
    a = 10
    b= 20
    return a+b
    
print("Result:",demo())
```

```python
def add():
    a = int(input("Enter a number"))
    b = int(input("Enter b number"))
    c = a + b
    return c
     
add()
```

```python
def sub():
    a = int(input("Enter a number"))
    b = int(input("Enter b number"))
    c = a - b
    return c
sub()
```

```python
#positional arguments or parameters passing in def function
def add(a,b):
    print(a+b)
    
add(1,2)
```

```python
def search(li,n):
    for i in li:
        if i == n:
            print(n,"value is present is the list")
            break
    else:
        print(n,"value is absent in the list")


l = [1,2,3,4,5,6,7]        
b = 5
search(l,b)
```

```python
def check(n):
    if n > 150:
        return "Large"
    elif n > 100 and n <= 150:
        return "medium"
    else:
        return "small"
    print("hello")            
    print("world") 
    
my_var = check(120)         #new variable for def function name
print(my_var)
```

```python
# default arguments 
# it is used to assingn a default argument value by passing in def function

def demo(a,b=5):    # here we assign default b = 5 inside the parameters of def functions so it mean default arguments     
    return a + b

result = demo(30)
print(result)
```

```python
def demo(a,b=5):   
    return a + b

result = demo(30,40)   # here we update the value of b by 40 inside the parameter of function name so it returns 70
print(result)
```

```python
def check(name,age):
    print("Hi",name,"your age is",age)
    
check("irfan",24)
```

```python
#keyword arguments
def check(name,age):
    print("Hi",name,"your age is",age)
    
check(age=24,name="irfan")    # mentioning the keys to the values that was already used after defining a function. 
                              # even after the paramenter value changes it position by assigning the right key inside the parameters.
```

```python
# arbitrary arguments
# n numbers of values will be passed by using this arbitrary arguments.
# (*argument)----> syntax for arbitrary arguments and its default datatype is tuple

def sum1(*val):
    print(type(val))
    print(val)
    print(sum(val))

sum1(1,2,4,5,6)
```

```python
# arbitrary keyword arguments
# n number of keys and values passed by using arbitrary keyword arguments
# (**argument)----> syntax for arbitrary keyword arguments and its default datatype is dictionary

def demo(**val):
    print(type(val))
    print(val)

demo(name="irfan",age=24,course="python")
```

```python
# order of all arguments
# in python it follows the order in functions by staring (positional arguments --> arbitrary arguments --> arbitrary keyword arguments)
# if we change this order it returns error

def demo(a,b,*val,**data):    # all of the arguments used here takes its own values used inside parameters of function name
    print("a =",a,"datatype-->",type(a))
    print("b =",b,"datatype-->",type(b))
    print("val =",val,"datatype-->",type(val))
    print("data =",data,"datatype-->",type(data))

demo(1,2,3,4,5,6,7,8,9,0,name = "irfan",age = 24 , course = "python")
```

# Simple Mini Calculator

```python
def addition(a,b):
    c = a + b
    return c
def subtraction(a,b):
    c = a - b
    return c
def multiplication(a,b):
    c = a * b
    return c
def division(a,b):
    c = a / b
    return c
def floor_division(a,b):
    c = a // b
    return c
def power(a,b):
    c = a ** b
    return c  

print("welcome to my calculator")
print("choose your options")
print("1 for add","2 for sub","3 for multiply","4 for division","5 for floor division","6 for power","7 for exit")
useroption = input("Enter your option")
if useroption == "1":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = addition(a,b)
    print("Your added result is",result)
elif useroption == "2":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = subtraction(a,b)
    print("Your subtracted result is",result)
elif useroption == "3":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = multiplication(a,b)
    print("Your multiplicated result is",result)
elif useroption == "4":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = division(a,b)
    print("Your divided result is",result)
elif useroption == "5":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = floor_division(a,b)
    print("Your floor_division result is",result)
elif useroption == "6":
    a = float(input("Enter the a number"))
    b = float(input("Enter the b number"))
    result = power(a,b)
    print("Your power value result is",result)
elif useroption == "7":
    print("come back soon")
else:
    print("invalid choice")
```
