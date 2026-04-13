# 5 - looping statements - for loop

```python
# 2. Looping Statements (Repetition)
'''
Looping statements are used to execute a block of code repeatedly.

              Types of Loops
--> for loop → when number of iterations is known
--> while loop → when repetition depends on a condition
--> Nested for Loop → a loop inside another loop

'''

# for loop
'''
for loop is finite loop that can controllable how many times that program wants to run.
Used to iterate over a sequence (like range, list, string).

for loop syntax ---->           for variable in iterable or generator:   |             iterable | generator
                                     statement 1...                      |         ---------------------------  
                                     statement 2...                      |           list        |   range
                                     statement 3...                      |           tuple       |    zip
                                     ... n number of statements....      |          dictionary   |    map
                                                                         |            set        |    filter
                                                                                     string      |                          '''


# for loop used in string

name = "Python"
for i in name:     # here i is iterating over the string and prints each character in line one by one 
    print(i)
```

```python
# range()

'''
range syntax has three parameters
range (start value , end value , step value)
            |             |           |
            |             |           |
    default = 0          n-1        default = 1
                         n+1
end value n-1 applied when step value 1 and n+1 appliesd when step value -1

1. single parameter ---> when single value is passed in the range it can take value has end value.

range(4) --> here 4 is end value , default start value = 0 and default end value = 1 -->(0,4,1). step value is 1 so end value applies n-1 which is (4-1)=3

so it runs or generates 4 values which is started from 0.

                                      range(4) --> (0,1,2,3).

2. two parameters ---> when two value is passed in the range it takes first value has start value and second value has end value.

range(2,8) ---> here 2 is start value which starts from 2 and 8 is end value and step value is default 1 so it applies n-1 which end value becomes 7.

                                    range(2,8) ---> (2,3,4,5,6,7)

3.three parameters ---> when three values is passed in the range it first value has start value and second value has end value and third value has step value

range(1,6,2)---> here 1 is start value and 6 is end value and 2 is step value . it applies n-1 because step value is positive 2 and end value becomes 5.

                                    range(1,6,2)---->(1,3,5) --> here step value is 2 which is stepping every 2 second value from the range
                                    

                                          -9 -8 -7 -6 -5 -4 -3 -2 -1 0  1  2  3  4  5  6  7  8  9 
                                          
step value---> +1 refers right direcrtion and -1 refers left direction
                       
range(2,6 -1) ---> () when start value is lesser than end value when step value is negative (-) it will empty

range(6,2,1) ---> () when start value is bigger than end value when step value value is positive (+) it will empty

inclusive --> 1 to 10 ---> output --> 1,2,3,4,5,6,7,8,9,10 (#we have to use +1 for the end value or use the value of the end value) (range(1,10+1)) or (range(1,11)).

exclusive --> 1 to 10 ---> output --> 1,2,3,4,5,6,7,8,9 (asusal (range(1,10)) it prints the values in range by n-1 formula and it depends on step value which is default +1.
```

```python
#range used in for loop
for i in range(3):            #here i = iter and range(3) = iterable. iter takes each value of iterable and goes into its statements.
    print("Hello")
```

```python
for i in range(3):    #here print("python") is not an for loop statement which is not in 4 space 
    print("Hello")
print("python")
```

```python
for i in range(3):  #here iter (i) takes first range value which is 0 and complete its all statements whic is print and goes for the second range value.
    print("Hello")
    print("Python")
```

```python
name=input("Enter a name")
for i in range(5):
    print(name)
```

```python
name=input("Enter the number")
number=int(input("Enter the number"))
for i in range(number):
    print(name)
```

```python
number=int(input("Enter a number"))
for i in range(1,number+1):       
    print(i)               #here print(i) because we have to print the iteration value till the user the value reach
```

```python
number=int(input("Enter a number"))
for i in range(1,number+1):       
    print(i,end=" ")               #here we have to set print(end=" ") to display the output in straight vertical line
```

```python
# To find odd or even
n=int(input("Enter a number"))
for i in range(1,n+1):
    if i%2==0:
        print(i,"Even")       #if modulous is used inbetween the first smaller and second greater number, the result will be the smaller number
    else:
        print(i,"odd",end=" ")
```

```python
#To fine square values ---->1st method
n=int(input("Enter a number"))
for i in range(1,n+1):
    square=i**2
    print(i,"->",square)
```

```python
#To fine square values ---->2nd method
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(i,"->",i*i)
```

```python
#string used in for loop
word="Irfan"
for i in word:    #here i the iter takes each character in word and print the each character which print called only i
    print(i)
```

```python
word="Irfan"
for i in word:   #The program assigns the string "Irfan" to the variable word. The for loop iterates through each character of the string. 
    print(word)   #However, instead of printing the current character (i), the program prints the entire string word in every iteration.
                   #Since the string contains five characters, the loop executes five times and prints "Irfan" five times
```

```python
#to find the vowels in string
word="Technical"
for i in word:
    if i in "aeiou":
        print(i)
```

```python
#to find the count of vowels
count=0                       #initially the count variable have to declare has 0 to count from 0
word="Technical"
for i in word:
    if i in "aeiou":
        count=count+1
        print(i)
print("Vowels count =",count)
```

```python
# to find the name by letter
name = ["malik", "irfan", "furkhan", "Mosina", "thasu"]
letter = input("Enter the first letter: ")

for i in name:
    if i[0] == letter:
        print("Your full name:", i)
    elif i[0]+i[1]==letter:
        print("Your full name:", i)
```
