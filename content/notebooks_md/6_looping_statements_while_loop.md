# 6 - looping statements - while loop

```python
# while loop

'''
 while loop is an infinite loop which is not have an destination when its condition gets true.  
 
   while loop syntax ---> 
                                    while condition(true or false):            (Runs as long as the condition is True)

                                           statement 1...
                                           statement 2...
                                           statement 3...
                                           number of statement... '''
```

```python
i=1  
while i<=5:     
    print(i)
    i=i+1             #here i value should be increment by +1 to break the infinite while loop
```

```python
i=5
while i>=1:
    print(i)
    i=i-1              #here i value should be decrement by -1 to break the infinite while loop
```

```python
i=5
while i!=0:      #here to change of condition and but having the same decrement output
    print(i)
    i=i-1
```

```python
#to find odd or even using while loop
i=1
while i<=10:
    if i%2!=0:
        print(i)
    i=i+1
```

```python
total=0
while total<=50:
    number=int(input("Enter the number"))
    total=total+number
print(total)
```

```python
#guessing game
target=65
user=int(input("Enter the number"))
while user!=target:
    if user>target:
        print("Too High")
    elif user<target:
        print("Too Low")
    user=int(input("Enter the number"))
print("Well Done")
```
