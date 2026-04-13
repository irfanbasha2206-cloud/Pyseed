# 13 - Data Structures  - set{ }

```python
#set is a collection of data which is unordered , unchangeable and unindexed and no duplicate members.

'''Description: 
              # Do not allow duplicate values only accepy unique values.
              # Duplicate values will be removed.
              # Any datatype can be stored in the set which is heterogeneous datatype
              # We cannot modify the set items.
              # We can only add or remove items. '''
              # Elements which are present inside set brackets {} that are considered as set


a = {1,2.3,4}
type(a)
```

| Method                        | Description                          | Example                     |
| ----------------------------- | ------------------------------------ | --------------------------- |
| `add(x)`                      | Adds one element                     | `s.add(3)`                  |
| `update(iterable)`            | Adds multiple elements               | `s.update([3,4])`           |
| `remove(x)`                   | Removes element (error if not found) | `s.remove(2)`               |
| `discard(x)`                  | Removes element (no error)           | `s.discard(2)`              |
| `pop()`                       | Removes random element               | `s.pop()`                   |
| `clear()`                     | Removes all elements                 | `s.clear()`                 |
| `union(other)`                | Combines sets                        | `a.union(b)`                |
| `intersection(other)`         | Common elements                      | `a.intersection(b)`         |
| `difference(other)`           | Elements in first not in second      | `a.difference(b)`           |
| `symmetric_difference(other)` | Non-common elements                  | `a.symmetric_difference(b)` |
| `issubset(other)`             | Checks if subset                     | `a.issubset(b)`             |
| `issuperset(other)`           | Checks if superset                   | `a.issuperset(b)`           |
| `isdisjoint(other)`           | No common elements                   | `a.isdisjoint(b)`           |

```python
# unordered 
a = {"apple",6,1,2,3,4,5}  # --> starts with number in output that is unorderd
a
```

```python
# unacceptance of duplicate value
a = {"apple",6,1,2,"apple",3,4,5 ,"apple"}
a
```

```python
# to remove duplicate values in list use type conversion of set
a = ["apple",6,1,2,"apple",3,4,5 ,"apple"]
print(a)
b = set(a)
print(b)
c = list(b)
print(c)
```

```python
# alternate methode by 1 line code by type coversion
a = ["apple",6,1,2,"apple",3,4,5 ,"apple"]
a = list(set(a))
print(a)
```

```python
# In set to add values use add function 
# add()
a = {1,2,3,4,5}
a.add(6)
a
```

```python
# In set to remove values use remove function 
# remove()
a = {1,2,3,4,5}
a.remove(5)
a
```

```python
# to remove the element and when the element already exit it ignores and it return not an error
a = {1,2,3,4,5}
a.discard(6)
a
```

```python
# to update the 1st variable with 2nd second variable use update function and even duplicates remove while updating
#update()
a = {1,2,3,4}
b = {5,6,7,8}
a.update(b)
a
```

```python
# to combine two sets and store into an new variable use union function, the symbol of union is "|"
# union()
a = {1,2,3,4}
b = {5,6,7,8}
c = a.union(b)
print(a)
print(b)
print(c)
```

```python
# by using symbol of union
a = {1,2,3,4}
b = {5,6,7,8}
c = a | b
c
```

```python
# to find the common in the two sets use intersection function. the symbol of intersection is "&"
# intersection()
a = {1,2,3,4}
b = {4,5,6,7}
c = a.intersection(b)
c
```

```python
# by using intersection symbol
a = {1,2,3,4}
b = {4,5,6,7}
a & b
```

```python
# intersection_update function is used update the left variable value by the right variable variable
# intersection_update()
a = {1,2,3,4}
b = {4,5,6,7}
a.intersection_update(b)
a
```

```python
#difference function is find out the values which is not common in the two sets
#difference()
a = {1,2,3}
b = {3,4,5,6}
c = a.difference(b)
c
```

```python
a = {1,2,3}
b = {3,4,5,6}
c = b.difference(a)
c
```

```python
# difference_update function is used find out the elements which are not same in two sets and it updated into superset variable
# difference_update
a = {1,2,3}
b = {3,4,5,6}
a.difference_update(b)
a
```

```python
a = {1,2,3}
b = {3,4,5,6}
b.difference_update(a)
b
```

```python
#symmetric_difference is used to find out the not common values of two sets
#symmetric_differece()
a = {1,2,3}
b = {3,4,5,6}
c = a.symmetric_difference(b)
c
```

```python
#symmetric_difference_update is used to find out the not common values of two sets and it updated left side variable 
#symmetric_difference_update
a = {1,2,3}
b = {3,4,5,6}
a.symmetric_difference_update(b)
a
```

```python
#isdisjoint fuction is to find out the common values that are present inside the set by revealing trur or false
#isdisjoint()
a = {1,2,3}
b = {3,4,5,6}
a.isdisjoint(b)   # there is a common value present inside the set (3) so it returns false
```

```python
a = {1,2,3}
b = {4,5,6}
a.isdisjoint(b)    # there is no common value present inside the set so it returns true
```

```python
#issubset function is to check if all the values of subset is contain in superset values by returning true or false
#issubset()
a = {1,2,3}     #-----------> Superset
b = {1,2,3,4,5,6}  #-------> subset
a.issubset(b)
```

```python
a = {1,2,3}     
b = {2,3,4,5,6}  
a.issubset(b)      #------> even if one value is not in subset it returns false
```

```python
#issuperset function is to check if all the values of superset is contain in subset values by returning true or false
#issuperset()
a = {1,2,3,4,5,6}     #-----------> Superset
b = {1,2,3}     #--------->subset
a.issuperset(b)
```

```python
a = {2,3,4,5,6}     #-----------> Superset
b = {1,2}     #--------->subset
a.issuperset(b)                     #------> even if one value is not in superset it returns false
```

```python
# set simple question
overall_stock = ["Dairy Milk" , "5 Star" , "Kitkat" , "Milky Bar", "Munch"]
current_stock = ["Dairy Milk" , "5 Star" , "Kitkat"]
out_of_stock = set(overall_stock).difference(set(current_stock))
out_of_stock = list(out_of_stock)
out_of_stock
```

```python
overall_stock = ["dairy milk", "5 Star", "kitkat", "milky Bar", "munch"]
current_stock = ["dairy milk", "5 Star", "kitkat" ]

choco = input("Enter the Chocolate: ")

if set(overall_stock).issubset(set(current_stock)):
    print("All stocks are available")
elif choco not in overall_stock:
    print(choco,"Chocolate not available")
else:
    out_of_tock = set(overall_stock).difference(set(current_stock))
    out_of_stock = list(out_of_stock)
    print(out_of_stock)
```

```python
overall_stock = ["dairy milk", "5 Star", "kitkat", "milky Bar", "munch"]
current_stock = ["dairy milk", "5 Star", "kitkat"]

choco = input("Enter the Chocolate: ")

if choco in current_stock:
    current_stock.remove(choco)

else:
    overall_stock = set(overall_stock).difference(set(current_stock))
    out_of_stock = list(out_of_stock)
    print("out_of_stock:",out_of_stock)
```
