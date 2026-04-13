# 4 -  Control statements - Conditional Statements

```python
# Control Statements in Python

'''
Control statements in Python are statements that control the flow of execution in a program.
They decide which statements execute, how many times, and in what order.

They were used to control the “flow” of the program, instead of executing sequentially.


                                                           Control Statements
                                                                  |
                 ------------------------------------------------------------------------------------------------------------------
                 |                                  |                                 |                                           |
      Conditional Statements                 Looping Statements                Jumping Statements                 Function Control Statements
                 |                                  |                                 |                                            |
                ->if                               ->for loop                        ->break                                      ->return
                ->else                             ->while loop                      ->continue                                   ->yield
                ->elif                             ->nested loop                     ->pass                                       ->raise
                ->nested if                                                            

This control statements controls the program in some ways to better peformance                                             


'''
```

| Category                              | Purpose                             | Keywords / Statements                                     |
| ------------------------------------- | ----------------------------------- | --------------------------------------------------------- |
| Conditional Statements                | Decision making                     | `if`, `if-else`, `if-elif-else`                           |
| Looping Statements                    | Repetition                          | `for`, `while`                                            |
| Jumping / Function Control Statements | Alter flow inside loops / functions | `break`, `continue`, `pass`, / `return`, `yield`, `raise` |

```python
# Conditional Statements (Decision Making)

'''
Conditional statements allow a program to make decisions based on conditions.
The condition is evaluated as True or False, and the program executes the corresponding block.
'''

# Types of Conditional Statements

'''
--> if
--> if-else
--> if-elif-else
--> Nested if
'''
```

```python
#if condition
# Executes code only if the condition is True.

'''if syntax --> if condition (true or false):

                                      if condition (true or false):                |          if 5>4:
                                      (4     Statement 1                           |              print("hello")     
                                      space  statement 2                           |              print("world")           
                                      or     statement 3                           |                    
                                      tab    statement 4..                         |
                                      space) ........n number of statements...     |
                                      
If condition is true it goes into its statements and if condition is false it ignores its statements and it goes for next line of execution'''
```

```python
x=2
if x>1:
    print("I")                  
    print("love")
    print("U")
    print("Python")
```

```python
x=2
if x>1:                    #here the condition satisfied with true and goes into its statements
    print("I")                 
    print("love")          #here these two statements are considered as if condition statements because it has 4 space after the condition 

print("U")                 
print("too") 
print("Irfan")             #here these two statements does not considered as if condition statements because it does not has 4 space
```

```python
x=2
if x>2:         #here the condition get fails and does not pass into its statement which represents in 4 space and it goes into the next line of execution which is not in 4 spaces 
    print("I")
    print("love")
    print("u")

print("sorry")
print("sissy")
print("I")
print("love")
print("coding")
```

```python
# else condition
# Chooses between two blocks.

'''It does not had any conditions and it depends on if and elif. if or elif gets false it directly goes into else condition and dispalys else statement 
syntax--> else:                                 
                                               else:                                        |       else:
                                        (4         Statement 1                              |          print("hello")      
                                         space)    statement 2                              |          print("world)
                                                   .....n number of statements.....         |'''
x=10
if x==12:                  #here if condition gets failed and it directly goes to the else part and displays the statements of else                   
    print("hello")
    print("java")
else:
    print("hello")
    print("python")
```

```python
#To find the input number is odd or even
number=int(input("Enter the number"))
if number%2==0:                              #any number is divisible by 2 and gives remainder 0 it is an even number
    print("The number is even")
else:
    print("The number is odd")
```

```python
# method 1 - simple
char=input("Enter a Alphabetic character: ") 
vowels="aeiou"
if char in vowels:                    #here in operator checks the given input charater was there in vowels
    print(char,"is an vowel")
else:
    print(char,"is an consonant")
```

```python
# method 2 - complex
char=input("Enter a alphabetic character: ")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":     '''here the comparison operator == compares the input with given vowels and or operator gets satisfied by one condition gets true
    print("vowels")
else:
    print("consonant")
```

```python
# elif condition --> else if 
# Used for multiple conditions.

'''elif syntax --> elif condition (true or false):

                                      elif condition (true or false):                |          elif 5>4:
                                      (4     Statement 1                           |              print("hello")     
                                      space  statement 2                           |              print("world")           
                                      or     statement 3                           |                    
                                      tab    statement 4..                         |
                                      space) ........n number of statements...     |
                                      
else depend on if condition. if condodition gets false it goes to next line of execution which is elif
elif condition is true it goes into its statements and elif condition is false it ignores its statements and it goes for next line of execution'''
```

```python
x=3
if x>1:               #here if condition gets true and elif also gets true. 
    print("python")     
elif x==3:
    print("java")     #By first condition if gets true it would print its statement even when elif condition also true because its all of an family
else:
    print("c++")
```

```python
# month start , middle and end

day = int(input("Enter the day"))
if (day>=1) and (day<=10):     #here and operator satisfies two conditions rather to use or operator. 
    print("Month Start")        
elif (day>=10) and (day<=20):   #when range used like (1 to 20) and operator performs.
    print("Month Middle")
elif day>=21 and (day<=31):      # (1 to 10) --> output --> 10 it is inclusive 
    print("Month End")           # (1 to 10) --> output --> 9 it is exlusive
else:
    print("Invalid Value")     #here if user gives any negative value , any characters in strings or any other special characters it returns invalid value
```

```python
x=2
if x<1:
    print("hello")
print("Monkey")         #here comes an error because inbetween if , else and elif we can't use individual line of codeliljc vfn'
else:
    print("python")
```

```python
#which is greater 

a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
if a>b:
    print("A is Greater")
elif b>a:
    print("B is greater")
elif a==b:
    print("Both A and B are Equal")
else:
    print("Invalid value")
```

```python
# nested if 
# An if inside another if.

'''if condition is used in if condition or elif condition is used in elif condition or if is used in elif condition is called nested if.'''

x=9
if x>7:          #here the given x value is satisfied in first if condition and does not satisfied in second if condition so it goes into else part(java)
    if x%2==0:
        print("Python")
    else:
        print("Java")
elif x<3:
    if x==1:
        print("Html")
    elif x==2:
        print("C++")
    else:
        print("Javascript")
else:
    print("C")
```

```python
x=7
if x<1:       # this if is indiviual family
    print("hello")
if x==2:               # these if and else are individual families
    print("python")
else:
    print("java")
```

```python
if True:                   #here if true means goes into its statments and execute
    print("Hello")
elif True:
    print:("Python")
else:
    print("Java")
```

```python
if False:
    print("hello")       #here if false means goes to the elif and elif execute its statement 
elif True:
    print("python")
else:
    print("java")
```

```python
if 1:
    print("rare")              #here 1 refers to ----> true and 0 refers to ---> false which is subnumeric of true and false
elif 0:
    print("care")
else:
    print("fare")
```
