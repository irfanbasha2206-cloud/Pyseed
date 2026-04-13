# 12 - Data Structures - dictionary{ }

```python
#dictionary is a collection of data which is ordered and changeable or mutable and no dupicate members allowed.

'''Description:
              # Do not duplicate members.
              # Duplicate value will overwrite existing value.
              # Any type of data type can be stored.
              # We call out the items in dictionary using {key : value} pair that would be called as items.
              # Example: {"name" : "Irfan" ,  "age" : 24   , "course" : "Python"} ---> this dictionary contains 3 items.
                            |         |         |     |          |           |
                           key      value      key  value       key        value

             # Keys should be in unique values because keys do not allows duplicate values but values allow duplicate members.
             # In dictionary keys should be in immutable datatype like string , integer and tuple wherelse values allowes any mutable and immutable datatype like list , float , and also dictionary 
             # Example:- a = {"apple" : [60,50,40] ,"kiwi" : {"local": 50 , "royal" : 100}} 
                                |         |           |          |     |       |       |
                                key      value       key        key  value    key    value
                              
             # Mostly In dictionary we used to call out ,  modify and add the values by default key
             # Example:- a = {"a" : 100 , "b" : 200 "c" : 300}
             # To call out the value in "a" --> a["a"] ---> displays ---> 100
             # To modify the value in "a" --> a["a"] = 500  ---> displays --- {"a" : 500}
             # To add the item assign a["d"] = 500
             # variable.keys to get keys in the dictionary
             # variable.values to get values in the dictionary
             # variable.items to get items in the dictionary and result will be tuple()
             # Dictionary{} ----> items in key : value pair that are present inside the curly braces {}  '''

a = {"a" : 100 , "b" : 200 ,"c" : 300}
type(a)
```

```python
# To call out the value 
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a["a"]
```

```python
#To modify the value 
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a["a"] = 500
a
```

```python
# To add the item
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a["d"] = 400
a
```

```python
# to get keys in the dictionary
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a.keys()
```

```python
# to get values in the dictionary
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a.values()
```

```python
# to get items in the dictionary
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a.items()
```

```python
# alternate method for get values in the list
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a.get("a")
```

```python
# loop in dictionary for constant as keys
a = {"a" : 100 , "b" : 200 ,"c" : 300}
for i in a:  # in this condition keys only printed 
    print(i)
```

```python
# loop in dictionary for values 
a = {"a" : 100 , "b" : 200 ,"c" : 300}
for i in a.values():  # to get values
    print(i)
```

```python
# loop in dictionary for items 
a = {"a" : 100 , "b" : 200 ,"c" : 300}
for i in a.items():  # to get items
    print(i)
```

```python
a = {"apple" : [60,50,40] ,"kiwi" : {"local": 50 , "royal" : 100}} 
print(a.items())
```

```python
# unpacking in dictionary
a = {"a" : 100 , "b" : 200 ,"c" : 300}
a.items()
for i,j in a.items():
    print(i,j)
```

```python
a = {"apple":300 , "orange":400 , "mango":500, "apple":600}
a    # ------> when duplicate members in dict they take last duplicate item value as first item value and it takes this as updated value
```

```python
# new element storing in empty dictionary
# student mark
marks = {}
for i in range(3):
    name = input("Enter the Name:")
    mark = int(input("Enter the Mark:"))
    marks[name] = mark
print(marks)
```

```python
#nested dictionary
a = {"stu1":{"chemistry":67,"maths":88,"physics":77} , 
     "stu2":{"chemistry":77,"maths":68,"physics":97}, 
     "stu3":{"chemistry":87,"maths":68,"physics":87}}
print(a["stu1"])
print(a["stu2"])
print(a["stu3"])
```

```python
a = {"stu1":[56,67,96], 
     "stu2":[89.67,88], 
     "stu3":[88,66,78]}

print(a["stu1"][2])     # by calling index number we can get the marks in the list used inside the dictionary
```

```python
#update fuction is used to update a set by b set by overwriting duplicate key and update its current value.
#update()
a = {1:24,2:45,3:56}
b = {3:66,4:78,5:88}
a.update(b)
print(a)
```

```python
#sum function is used to add the values inside the dictionary by using key
#sum()
a = {1:23,2:33,3:54,4:45,5:55}
b = sum(a.values())
print(b)
```

```python
#max function is used to get the maximum value by using key
a = {1:23,2:33,3:54,4:45,5:55}
max(a.values())
```

```python
# to count the each character in the string and display the output in string
a = "apple"
char_count = {}

for i in a:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)
```
