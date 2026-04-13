# 9 - Data Structures - strings and functions

```python
# Data Structures

'''
A data structure is a way of organizing and storing multiple data items so they can be used efficiently.

A data structure can hold multiple values. Some data structures are mutable (can be changed), some immutable. 


--> Key Difference Between Data Type and Data Structure

| Aspect     | Data Type                                  | Data Structure                                                    |
| ---------- | ------------------------------------------ | ----------------------------------------------------------------- |
| Definition | Type of a single variable (int, str, bool) | Organized way to store multiple data items                        |
| Scope      | Single value                               | Multiple values                                                   |
| Mutability | Can be mutable or immutable                | Some mutable (list, set, dict), some immutable (tuple, frozenset) |
| Examples   | int, float, str, bool                      | list, tuple, dict, set, string                                    |


Conclusion:

Data type → Tells Python what kind of data a variable holds.
Data structure → Tells Python how to store and organize multiple pieces of data efficiently.

'''
```

```python
# String 

'''

A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).

Strings are ordered (each character has an index).
Strings are immutable (cannot change individual characters).
Strings support many operations and methods, making them a versatile data structure.

Strings can be applied in lists , tuple , set and dictionary.

1. Indexing                                           

indexing means accessing individual characters of a string using their position (index number).

Syntax of indexing ---> variable [number] --> a[0]


                                                                    indexing
                                                                      |
                                                                      |
                                                             ------------------- 
                                                             |                 |
                                                    positive indexing        negative indexing
                                                     starts with 0             ends with -1
                                                       
                                                     a="hello"               a =" h e l l o "   
                                                        01234                    -5-4-3-2-1               '''
a = "cookie"
type(a)
```

```python
# Single quotes
str1 = 'Hello'

# Double quotes
str2 = "Python"

# Triple quotes (for multi-line strings)
str3 = '''This is
a multi-line
string.'''

print(str1)
print(str2)
print(str3)
```

```python
#positive indexing
a="hello"
a[4]
```

```python
#negative indexing
a="hello"
a[-1]
```

```python
'''a="hello"
a[7] ----> out of index error''
```

```python
'''2. slicing 
String slicing is used to extract a part (substring) of a string by specifying a range of indexes.

syntax of slicing ---> [start value : end value : step value]
                            0          n-1 & n+1       1           '''
```

```python
#positive slicing
a="Hello"
a[0:3]    # here end value 3 default step value +1 so end value applies n-1 (3-1=2) so from 0 index to 2nd index character would be sliced.
```

```python
a="Hello"
a[1:4]
```

```python
a="hello"
a[0:5:2] # here step value 2 so it stepped every second character from start value to end value
```

```python
a="hello"
a[:5]   #here only end value is given start and step value is default 0 and 1 so it slices the whole charcter
```

```python
a="hello"
a[:2]
```

```python
a="hello"
a[1:]   # here end value and step value not given so it takes up to end
```

```python
a="hello"
a[1:7]   # here being in out of index value slice works upto end
```

```python
a="Hello"
a[:]    # no start value and end value and it slice from start to end
```

```python
a="hello"
a[::]  # no start value and end value and  no step value it slice from start to end
```

```python
#negative slicing
a="Hello"
a[-4:-1]
```

```python
a="Hello"
a[4:0:-1]
```

```python
#string reverse by slicing
a="hello"
a[::-1]
```

```python
# string inbiuld fuctions
''' common function 
--> len() -->  is used to get the number of character in a string
Eg --> a= "hello" --> len(a) --> 5 '''
```

```python
a="hello"
len(a)
```

```python
#upper function is used to capitals all the character in that string 
#upper() 
a = "hello"
a = a.upper()
```

```python
a
```

```python
#lower funtion is used to lower all the character in that string
#lower() 
a="HELLO"
a=a.lower()
```

```python
a
```

```python
#capitalize funtion is used to capital the first character of that string
#capatalize() 
a="hello"
a=a.capitalize()
```

```python
a
```

```python
#title fuction is used to title of every words first letter in that string
#title() 
a="hello world"
a=a.title()
```

```python
a
```

```python
#replace function is used to replace the particular character in that string
#replace() 
a="hello"
a=a.replace("h","H")
```

```python
a
```

```python
#find function is used to find the particular character by first in that string and it reveals the index position
#find() 
a="hello enter"
a=a.find("e")
```

```python
a
```

```python
a="hello enter"  # to find 2nd e use index after that e
a=a.find("e",2)
```

```python
a
```

```python
#count function is used to count the particular character in that string
#count() 
a="hello"
a=a.count("l")
```

```python
a
```

```python
a="hello world"   # to count the particular character by argument indexing
a=a.count("l",3)
```

```python
a
```

```python
a="hello world"   # by counting of index number 5 there is no "e" so it returns 0
a=a.count("e",5)
```

```python
a
```

```python
#strip function is used to remove the unwanted spaces
#strip () 
a = "    Hello    "
a=a.strip()
```

```python
a
```

```python
#left strip function is used to remove the unwanted space at left side at the end of the string
#lstrip() 
a = "    hello   "
a=a.lstrip()
```

```python
a
```

```python
#rights trip functiom is used to remove the unwanted space at right side at the end of the string
#rstrip()
a = "   hello     "
a=a.rstrip()
```

```python
a
```

```python
a = "    hello    world    "
a=a.strip()                    # it could not remove the space inbetween the string
```

```python
a
```

```python
#split funtion is used to convert the string into list each words are individual element
#spilt()
a = "Hello world python"
a=a.split()
```

```python
a
```

```python
war = "American War"
Zwar= war.split()      # here spilt has to stored into a new variable to iterate each individual element
for i in Zwar:
    print(i)
```

```python
#individual character spliting
a="hello  world  python"
a=a.split("o")
```

```python
a
```

```python
a="hello  world  python"
a=a.split("l")    # here l is present two times in first element as besides of each other so it contains of an empty string
```

```python
a
```

```python
#isupper function is used to find the sequence of given all charcters contains only in upper case by revealing true or false
#isupper()
a="HELLO WORLD"
a=a.isupper()
```

```python
a
```

```python
#islower function is used to find the sequence of given all charcters contains only in lower case by revealing true or false
#islower()
a="hello world"
a=a.islower()
```

```python
a
```

```python
#isaplha function is used to find the given all characters are containing only in alphabets by revealing true or false
#isalpha()
a="Hello br@"
a=a.isalpha()
```

```python
a
```

```python
#isnumeric function is to find the given all characters are containing only in numbers by revealing true or false
#isnumeric()
a="12356"
a=a.isnumeric()
```

```python
a
```

```python
#isalnum function is to find the given all characters are containing only in alphabets and also either in numbers by revealing true or false
#isalnum()
a="hello123"
a=a.isalnum()
```

```python
a
```

```python
a="hello 123"
a=a.isalnum()     # here inbetween hello and 123 there is space so it reveals false
```

```python
a
```

```python
#join function is used to combine elements of an iterable (like a list, tuple, or set) into a single string, using a specified separator string.
#join()
words = ["Python", "is", "fun"]
result =" ".join(words)
print(result)
```

```python
#string concatenation
war="w"+"orld"
war=war.capitalize()
```

```python
war
```
