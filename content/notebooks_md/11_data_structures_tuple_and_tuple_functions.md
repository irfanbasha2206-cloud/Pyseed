# 11 - Data Structures - tuple( ) and tuple functions

```python
#tuple is a collection of data which is ordered and unchangeable or immutable and it allows duplicate members

'''Description:
          # Allows duplicate.
          # Any type of data can be stored.
          # we cannot modify the tuple item which is immutable.
          # we cannot add or remove in the tuple.
          # we can only delete the entire tuple. 
          # tuple is faster than list because it is an contigeous memory which stores data next to each other in memory without gaps .
          # so the value retreive process will be fast
          # It is an heterogenous datatype which stores data also in mixed datatype.
          # mainly we use in loop through tuple because it is faster
          # in real time there are millions of data so we use tuple to enchance this to makes application and websites faster
          # tuple() ----> elements that are present inside the parenthesis () and also the sequence of values with "," without "()"   '''

a = (1,2,3,4,5)   # --->  values with "()"
(type(a))
```

```python
a = 1,2,3,4,5   # --->  values with "," without "()" 
(type(a))
```

```python
# functions or methods used in tuple
#count()
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))
```

```python
# index
t = (10, 20, 30, 20)
print(t.index(20))
```

```python
# Useful Built-in Functions That Work With Tuples
'''| Function   | Purpose                               |
   | ---------- | ------------------------------------- |
   | `len()`    | number of elements                    |
   | `max()`    | largest value                         |
   | `min()`    | smallest value                        |
   | `sum()`    | total of elements                     |
   | `sorted()` | sorts values and result will be list  |
   | `tuple()`  | converts to tuple                     |'''

t = (1, 2, 3, 4)
u = [1,2,3,4]

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t,reverse=True))
print(tuple(u))
```

```python
# tuple unpacking
a,b = (1,2)
b
```

```python
a,b = (1,2)
c = a,b
print(tuple(c))
```

```python
a,b = (1,2,3)
c = a,b         
print(tuple(c))    #error ---> many values to unpack
                  # while unpacking the variable count is equal to the tuple value count
```

```python
a = (1)   #tuple will follow more than one value even though when it is also inside ()
type(a)
```

```python
a = (1,2)   
type(a)
```

```python
a = (1,)  # when we want our single value to be stored has tuple use "," after the value
type(a)
```

```python
#type conversion in data structures
a = (1,2,3,4)
a = list(a)
print(a)
```

```python
a  = (1,2,3,4)
b = 5
a = list(a)   # covert it to list
a.append(b)      # and append it to list
a = tuple(a)      # convert it to tuple
print(a)
```

```python
# tuple concatenation
a = (1,2,3,4)
b = (5,)
c = a + b
print(c)
```

```python
a = (1,2,3,4,5)
del a     # to delete the whole tuple
a
```

```python
# loop in tuple
a = (1,2,3,4,5)
for i in a:
    print(i)
```
