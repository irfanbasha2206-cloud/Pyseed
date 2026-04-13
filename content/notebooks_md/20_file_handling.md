# 20 - File Handling

```python
# File handling

'''File handling is the process of storing, retrieving, and modifying data in files instead of keeping everything in memory.

1. Usefullness of  File handling

--> Data in variables is temporary
--> Files provide permanent storage
--> Useful for logs, reports, user data, etc.

2. Types of Files

 Text Files 
-->Store data in readable format
-->Data is stored as characters in extentions
--> extentions (.txt) (.csv) (.json)
--> data storage of each extention

| File Type | Full Form                  | What it Stores                | Structure                 | Example Content             | Best Use                     |
| --------- | -------------------------- | ----------------------------- | ------------------------- | --------------------------- | ---------------------------- |
| `.txt`    | Text File                  | Plain text (any data)         | No structure              | Hello World                 | Notes, logs, simple data     |
| `.csv`    | Comma-Separated Values     | Tabular data (rows & columns) | Structured (table format) | name,age<br>John,25         | Excel-like data, datasets    |
| `.json`   | JavaScript Object Notation | Key-value data                | Structured (nested)       | {"name": "John", "age": 25} | APIs, configs, data exchange |



 Binary Files
-->Store data in binary (0s and 1s)
-->Examples: images, videos, executables
-->Not human-readable 
--> extention (.bin) (.dat)
--> modes "rb --> read binary
          "wb" --> write binary
          "ab" --> append binary
        
--> Modes can be combined:
example:-  

--> "rb+" --> read & write (no overwrite and file must exist)
--> "wb+" --> write & read (creates and overrites file)
--> "ab+" --> append & read (creates file if not exits)          '''
```

```python
'''

3. File Modes (Important Concept)

File modes define how the file will be used.

| Mode | Meaning                             |
| ---- | ----------------------------------- |
| `r`  | Read only                           |
| `w`  | Write (overwrites existing content) |
| `a`  | Append (adds content at end)        |
| `x`  | Create new file                     |
| `b`  | Binary mode                         |
| `t`  | Text mode (default)                 | 




4. Basic commands to access files via command prompt

|     Command     |   Use                  |    Simple Meaning            |
| --------------- | ---------------------- | ---------------------------- |
| `dir`           | List files and folders | Show what is inside a folder |
| `cd`            | Change directory       | Move between folders         |
| `mkdir` / `md`  | Create folder          | Make a new folder            |
| `rmdir` / `rd`  | Remove folder          | Delete a folder              |
| `del` / `erase` | Delete file            | Remove a file                |
| `copy`          | Copy files             | Make a duplicate file        |
| `xcopy`         | Copy folders           | Copy big folders easily      |
| `robocopy`      | Advanced copy          | Smart and fast copying tool  |
| `move`          | Move files/folders     | Shift file to another place  |
| `ren`           | Rename files           | Change file name             |
| `type`          | Display file content   | Show what’s inside a file    |
| `attrib`        | Change attributes      | Hide or protect files        |   


5. Navigate Directories 

|  Command            |          Use              | Simple Understanding                         |
| ------------------- | --------------------------| ---------------------------------------------|
|  `pwd`              | Show current directory    | “Where am I right now?”                      |
|  `ls`               | List files/folders        | “What’s here?”                               |
|  `cd foldername`    | Move into a folder        | “Go inside this folder”                      |
|  `cd ..`            | Go back one level         | “Go to parent folder”                        |
|  `cd`               | Go to home directory      | “Go to my main folder”                       |
|  `ls -l`            | Detailed list             | Shows size, permissions, date                |
|  `ls -a`            | Show hidden files         | Includes files starting with `.`             |
| `cd /path/to/folder`| Absolute path navigation  | Jump directly to full path                   |
|  `cd -`             | Go to previous directory  | Toggle between last two folders              |
|  `tree`             | View folder structure     | Visual tree of directories                   |    '''
```

```python
''' 
6. File Operations

File handling mainly involves 4 operations:

|. Open a file

Before working with a file, it must be opened.


||. Read a file
Read file has three operations 

--> Read()
--> Readline()
--> Readlines()

Retrieve data from the file.

|||. Write/Append to a file

Store or modify data in the file.


||||. Close a file

Release system resources after use.                                 '''
```

```python
# 1 read
''' 
Used to read content
File must already exist                 '''

# read() 

'''Read entire file
Reads the whole file content at once
Returns a single string '''

file = open(r"C:\Users\ELCOT\PYTHON\py0.txt")         # copy the path from directory and paste it.
file.read()
```

```python
''' 
7. File Object

When you open a file, Python creates a file object.

This object:

Controls file operations
Keeps track of file state (open/closed)
Provides methods like read, write, etc.      '''

file = open(r"C:\Users\ELCOT\PYTHON\py1.txt")
```

```python
file.read()
```

```python
'''
8. File Pointer Concept

When a file is opened, Python uses a file pointer:

It indicates the current position in the file
Moves automatically when reading/writing

--> Example idea:

Start → pointer at beginning
After reading → pointer moves forward'''

file.read()       # by reading the same file again while i run it would leads to empty
```

```python
# to overcome this use file.seek() and file.read() to read the file again
file.seek(0)          # here 0 is the index position when we 0 it starts from starting letter 
file.read()
```

```python
file.seek(19)      # it starts to read from index position 19 which has the letter "F"
file.read()
```

```python
''' 
9. Closing a File

Closing a file is important because:

Frees system memory
Ensures data is saved properly
Prevents file corruption

--> Python provides automatic closing using context management (with concept).  '''




file = open(r"C:\Users\ELCOT\PYTHON\py1.txt")   # when we paste the path backward slash "\"  would come along with file path and this would leads to error
file.read()                                       # we would change to forward slash "/" slash to open that file or 
file.close()                                          # we use "r" infront of double quotes
```

```python
# when we directly read the line it shows "\n" newline character along with the text 
# to overcome this newline character along with the text assign it to an variable and call it
# this simple method will be used only in read()

                                                      # "r" read mode is set default inside when we also not specify it
file = open(r"C:\Users\ELCOT\PYTHON\py1.txt","r")   # specify the operations like  "r" at last to understand the File Modes
content = file.read()  
print(content)
file.close()          # it is mandatory to close the file whenever we open it.
```

```python
# readline()

'''Read one line at a time
Reads only one line per call
Returns a string (with \n at end)'''

file = open(r"C:\Users\ELCOT\PYTHON\py2.txt","r")
```

```python
file.readline()
```

```python
file.readline()  # reads the second the while i run it
```

```python
file.readline() # reads the third line which is empty because there is no third third
```

```python
# readlines() 

''' Read all lines into a list
Reads entire file
Returns a list of strings (each line is an item) '''

file = open(r"C:\Users\ELCOT\PYTHON\py3.txt","r")
```

```python
file.seek(0)
file.readlines()
file.close()
```

```python
# to remove the \n we in readlines() we use logic
# 1st method

file = open(r"C:\Users\ELCOT\PYTHON\py3.txt","r")
file.seek(0)
dream = file.readlines()
dream1 = []

for i in dream:
    if "\n" in i:
        dream1.append(i[:-1])
    else:
        dream1.append(i)
file.close()
print(dream1)
```

```python
#2nd method for better performance

file = open(r"C:\Users\ELCOT\PYTHON\py3.txt","r")
file.seek(0)
val = file.readlines()
new = []

for i in range(len(val)):
    if i == len(val) -1:
        new.append(val[i])
    else:
        new.append(val[i][:-1])
file.close()
print(new)
```

```python
# 2 (a) write
'''
--> In write operation by entering the name of non existing file it creates it as new file
--> By pasting the same path of read in write mode it can overwrite the new lines by write on it
--> Used to write new content
--> Deletes existing content                               '''

file = open(r"C:\Users\ELCOT\PYTHON\py1.txt","w")     # specified "w" mode to understand it was an write file
file.write("Thank you for watching\n welcome again..!") 
file.close()
```

```python
# creating a new text file inside the path
file = open(r"C:\Users\ELCOT\PYTHON\py4.txt","w")     
file.write("Thank you for watching\n welcome again to watch..!") 
file.close()
```

```python
# (b) append
''' 
--> In append operation by entering the name of non existing file it creates it as new file
--> append mode is to stack or add new extra data to the new file or old file 
--> Used to add content at the end
--> Keeps existing data safe                              '''

file = open(r"C:\Users\ELCOT\PYTHON\py5.txt","w")     
file.write("Top 3 programming languages ..!") 
file.close()
```

```python
file = open(r"C:\Users\ELCOT\PYTHON\py5.txt","a")     # specify "a" mode to add additional data to the existing file
file.write("\npython \njava \nc++") 
file.close()
```

```python
'''
10. Context Manager (with) 

Instead of manually opening/closing files:

Python uses a context manager
It automatically handles closing
Prevents errors like forgetting to close files

--> This is considered the standard approach in modern Python '''

with open(r"C:\Users\ELCOT\PYTHON\py1.txt","r") as file:
    content = file.read()
    print(content)
```

```python
''' 11. Advantages of File Handling
Permanent data storage
Easy data sharing
Efficient for large data
Supports structured formats (CSV, JSON)


12. Common Issues in File Handling

While working with files, problems may occur:

File not found
Permission denied
File already exists
Data corruption

--> These are handled using exception handling                               '''
```
