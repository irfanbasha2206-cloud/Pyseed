# 10  - Data Structures - list[ ] and list function and 2D list

```python
#list is a collection of data which is ordered and changeable and mutable and it allows duplicate members.

'''Description: 
          # Allows duplicate.
          # Any type of data can be stored.
          # we can modify the list item.
          # we add or remove in the list.
          # list is slower than tuple because it is an Scattered memory.
          # Scattered memory means data stored in different places in memory, not next to each other.
          # so the value retreive process will be slow.
          # It is an heterogenous datatype which stores data also in mixed datatype.
          # 1,2,3,5,6]---> homogenous datatype which contains only one datatype in a list 
          # [1,2,3,"python","java",3.2,4.0,true,false] -----> hetrogeneous datatype which contains mixed datatype in a list
          # list[]----> whatever elements that are present inside the square bracket [] that is considered as list'''

a = [1,2,3,4]
type(a)
```

```python
a = [1,2,3,4,"py","java",4.5,6.7]
a = a[4]   # indexing "here in the index position 3 the element 4 is presented"
a
```

```python
a = [1,2,3,4,"py","java",4.5,6.7]
a=a[:3]   # slicing "here from default start index value 0 to end index value 3 by step value +1 it applies n-1 and end index valuue becomes 2 so it slices from 0 to 2"
a
```

```python
# List functions

'''| Method      | Description               |
   | ----------- | ------------------------- |
   | `append()`  | Adds element at end       |
   | `extend()`  | Adds multiple elements    |
   | `insert()`  | Inserts element at index  |
   | `remove()`  | Removes specific value    |
   | `pop()`     | Removes element by index  |
   | `clear()`   | Removes all elements      |
   | `index()`   | Finds position of element |
   | `count()`   | Counts occurrences        |
   | `sort()`    | Sorts list                |
   | `reverse()` | Reverses list             |
   | `copy()`    | Copies list               |  '''
```

```python
#append function is used to Adds an element at the end of the list.
#append()
a = [1,2,3,4]
a = a.append(5)
```

```python
a
```

```python
#remove function is used to Removes the first occurrence of a value by giving value not index. 
a = [1,2,3,4,2]
a.remove(2)
a
```

```python
#insert function is used to Insert an element at a specific position by index value and then element inside the parameters.
#insert()
a = [1,2,4,5]
a.insert(2,3)
a
```

```python
#pop function is used to Removes the last element in the list. it can also removes by giving index value inside parameters
#pop()
a = [1,2,3,4,3]
a.pop()
a
```

```python
a = [1,2,3,4,3]
a.pop(0)   # here by index value 0 it removes the 1 element in the list
a
```

```python
#count function is used to Counts how many times an element appears in the list by passing the value inside the parameter.
#count()
a = [1,2,3,4,2,5,2,6]
a = a.count(2)
a
```

```python
#index function Returns the index of the first occurrence of an element by passing the list element value.
#index()
a = [1,2,3,4,5,2]
a = a.index(3)
a
```

```python
#extend function Adds multiple elements from another iterable list to the first list by passing the list varaible inside the parameter. 
'''Simply merge two lists and update into the first list''' 
#extend()
a = [1,2,3]
b = [4,5,6]
a.extend(b)
a
```

```python
#sort function is used to Sorts the list default in ascending order and updated in the first list variable.
#sort()
#ascending sort
a = [9,8,7,6,5,4,3,2,1]
a.sort()
a
```

```python
#descending sort
numbers = [5, 2, 9, 1, 7]
numbers.sort(reverse=True)   #here 'reverse = true' is used to sort the number in descending order
print(numbers)
```

```python
#reverse function is used to Reverses the order of elements.
#reverse()
numbers = [1,2,3]
numbers.reverse()
print(numbers)
```

```python
#copy function is used to Returns a copy of the list.
#copy()
a = [1,2,3]
b = a.copy()
print(b)
```

```python
#list concatenation
a = [1,2,3]
b = [4,5,6]
c = a+b
c
```

```python
#list reputation
a = [1,2,3]*2
a
```

```python
[0]*5
```

```python
nuke_countries = ["america","russia","israel","pakistan","china","france","united kingdom","india","north korea"]
while True:
    user_input = input("Enter the nuke country")
    if user_input in nuke_countries:
        print("yes u did it ")
        break
    else:
        print("no u guess the wrong nuke country")
```

```python
nuke_countries = [
    "america", "russia", "israel", "pakistan",
    "china", "france", "united kingdom",
    "india", "north korea"
]

print("🌍 Welcome to the Nuclear Guess Game 🚀")

while True:
    user_input = input("🔎 Enter a nuclear country: ").strip().lower()

    if user_input in nuke_countries:
        print("✅ Boom! Correct guess 💥")
        break
    else:
        print("❌ Oops! That's not it. Try again 🔁")
```

```python
nuke_countries = [
    "america", "russia", "israel", "pakistan",
    "china", "france", "united kingdom",
    "india", "north korea"
]

print("🌍 Welcome to the Nuclear Guess Game 🚀")

while True:
    user_input = input("🔎 Enter a nuclear country: ").strip().lower()

    if user_input in nuke_countries:
        print("✅ Boom! Correct guess 💥")
        break
    else:
        print("❌ Oops! That's not it. Try again 🔁")
```

```python
# to change the particular value in the list by indexing
a = [12,2,3,4,5]
a[0] = 1
a
```

```python
#for loop using in list to check if whether number even or odd
a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in a:
    if i%2==0:
        b.append(i)
print(b)
```

```python
#to remove duplicate values in the list by using "not in" operator
a = [1,2,2,3,4,5,5,5,5]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
```

```python
#to remove duplicate by using set
a = [1,2,2,3,4,5,5,5,5]
b = list(set(a))
print(b)
```

```python
a = ["python" , "go" , "java"]
for i in range(len(a)):
    print(a[i])
```

```python
# to create list inside list
a = [1,2,3,4]
b = [5,6,7,8]
a.append(b)
a
```

```python
#sum of the values in the list
a = [1,2,3,4,5,6]
sum = 0
for i in a:
    sum = sum + i
sum
```

```python
# odd numbers sum values
a = [1,2,3,4,5,6,7,8,9,10]
b = []
add = 0
for i in a:
    if i%2!=0:
        add = add + i
        b.append(i)
print(b)
print(add)
```

```python
# min value in the list
a = [89,45,34,23,12,49,22]

min_val = a[0]

for i in a:
    if i < min_val:
        min_val = i

print("Minimum value:", min_val)
```

```python
# max value in the list
a = [89,45,34,23,12,49,22]

max_val = a[0]

for i in a:
    if i > max_val:
        max_val = i

print("Maximum value:", max_val)
```

```python
# sort the list without using sort() or sorted()
a = [12,3,4,9,6,2]

n = len(a)

for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            # swap
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("Sorted list:", a)
```

```python
'''2d list or 2dimensional list
a = [1,2,3,4,5,6] ---> 1d list
a = [[1,2,3],[4,5,6]] ---> 2d list '''

# to get the element in 1d list
a = [1,2,3,4,5,6]
a[3]
```

```python
# to get the element in 2d list
a = [[1,2,3],[4,5,6]]           
a[1][0]
```

```python
a = [[1,2,3],[4,5,6]]           
for i in a:
    print(i)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in a:
    for j in i:
        print(j)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in a:
    for j in i:
        print(i)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in a:
    for j in i:
        print(i[0])
```

```python
a = [[1,2,3],[4,5,6]]           
for i in range(len(a)):
    print(i)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in range(len(a)):
    print(a[i])
```

```python
a = [[1,2,3],[4,5,6]]           
for i in range(len(a)):
    for j in range(len(a[i])):
        print(j)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in range(len(a)):
    for j in range(len(a[i])):
        print(i,j)
```

```python
a = [[1,2,3],[4,5,6]]           
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
```

```python
# unpacking in list 
a,b,c = [1,2,3]  # the number of variables is exactly equal to the number of values
print(a,b,c)
```
