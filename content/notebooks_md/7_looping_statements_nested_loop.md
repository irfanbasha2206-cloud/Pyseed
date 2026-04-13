# 7 - looping statements - nested loop

```python
# Nested Loop 

'''
A nested loop means a loop inside another loop. that is repetition inside repetition

The inner loop runs completely every time the outer loop runs once.
Used for working with patterns, matrices, tables, combinations, etc.

'''

# Basic Structure Example

for outer in range(n):
    for inner in range(m):
        # code block
```

```python
# Simple Example Nested for Loop

for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)
```

```python
for i in range(3):      #--> outer loop
    for j in range(2):    #--> inner loop
        print(j)         #once inner loop complete (j) its all range values with its statements and it goes for outer loop (i)
```

```python
for i in range(3):
    for j in range(2):
        print(i)
```

```python
for i in range(3):
    for j in range(2):
        print(j)      #here j loop complete its range value by 1st iteration when i=0 then j=0 and j=1 and then goes for the next statement which is hello
    print("Hello")
```

```python
for i in range(3):
    for j in range(2):   #when i=0 then j=0 , j=hello python and j=1 , j=hello python and goes for next individual statement
        print(j)
        print("Hello Python")  #outer loop decide the overall statements and inner loop how many times gonna be work
    print("hello")
```

```python
for i in range(2):
    print("*******")
    for j in range(3):
        print(j)
    print("######")
```

```python
for i in range(3):
    for j in range(2):
        print(i)
        print(j)  
                          '''Step-by-Step Execution
When i = 0

j = 0 → prints i=0 , j=0

j = 1 → prints i=0 , j=1

When i = 1

j = 0 → prints i=1 , j=0

j = 1 → prints i=1 ,j=1

When i = 2

j = 0 → prints i=2 , j=0

j = 1 → prints i=2 ,j=1  '''
```

```python
for i in range(3):
    for j in range(2):
        print(j)
    print(i)
```

```python
for i in range(3):
    for j in range(2):
        print(j)
        print(i)
```
