# 22 - Modules , Libraries and Framework

# Difference Between Modules and Libraries

'''

| Feature    | Module                               | Library                                                   |
| ---------- | ------------------------------------ | ----------------------------------------------------------|
| Definition | A single file containing Python code | A collection of multiple modules                          |
| Size       | Small (one file)                     | Large (many files/modules)                                |
| Purpose    | Performs a specific task             | Provides a wide range of functionalities                  |
| Structure  | `.py` file                           | Folder/package with many modules                          |
| Example    | `math.py`, `random.py`               | `Standard Library`, `numpy`, `pandas`, `matplotlib`       |
| Usage      | `import math`                        | `import numpy`                                            |
| Scope      | Limited functionality                | Broad functionality                                       |

```python
# Python Modules / Libraries can be categorized into 4 main types:

'''
--> Built-in Modules

--> Standard Library Modules

--> User-defined Modules / Libraries

--> Third-party Modules / Libraries
```

```python
# Modules
'''
--> A module is simply a file containing Python code (functions, variables, classes) that you can reuse in other programs.
Module = reusable Python file

--> You can use a module in a four different way


1. Importing a module (Basic syntax)
   You import the module, then use module_name.function

 '''

import math

print(math.sqrt(16))

'''
2. Import specific items from the module
   No need to write math. every time
   
 '''
from math import sqrt

print(sqrt(25))

'''
3. Import with alias (shortcut name)
   Useful for long module names
'''

import math as m

print(m.sqrt(36))


'''
4. Import everything (rare usage)
   Can cause confusion if names clash
'''

from math import *

print(sqrt(49))

# Check what’s inside a module

import math

print(dir(math))
```

```python
#  User defined modules

# A user-defined module is a module that is created by the programmer, rather than being provided by Python’s standard library.

# for example

def add(a, b):  
    return a + b   # save this file to resue as a module


import mymodules    # importing a user-defined module

print(mymodule.add(2, 3))


# 2.  user_defined module usecase
# a. Import from another folder


from folder_name import mymodules

# b.  Or modify path:

import sys
sys.path.append("path_to_folder")
import mymodules
```

```python
# examples of user defined modules

from mymodule import Car        
                                                # car class is saved in mymodule file whenever its needed it would be imported and reused
car1 = Car("innova",2016,"white",500000)
print(car1.name)
print(car1.model)
print(car1.color)
print(car1.price)

print()

car2 = Car("Audi",2016,"black",900000)    # it is reused for 2nd object also 
print(car2.name)
print(car2.model)
print(car2.color)
print(car2.price)
```

```python
import importlib    # To add and get methods in user define module use importlib library to reload for syncing together 
                     # to access the methods in class
import mymodule

importlib.reload(mymodule)

from mymodule import Car

car1 = Car("cybertruck",2024,"silver",5000000)     
car1.drive()                                          # init instance variable is used in normal method in mymodule and it is hided
print()
car2 = Car("Audi",2016,"black",900000)
car2.drive()
```

```python
#  Built-in modules

'''
Built-in modules are modules that come pre-installed with Python.
Built-in modules are those compiled into the Python interpreter and available by default.

Comes preloaded with Python
Usually written in C (for speed)
Provides core functionality of Python
Some are available without importing, others need import


Common Built-in Modules (Important Ones)

1. Core / System
sys – System-specific parameters and interact with Python runtime
builtins – Built-in functions like print(), len()


2. gc – Garbage collection
atexit – Run code when program exits


3. Data Types & Utilities
itertools – Iterator tools
functools – Higher-order functions
operator – Functional operators
types – Dynamic type checking


4. Mathematics
math – Mathematical functions
cmath – Complex math

 
5. Interpreter & Execution
__main__ – Entry point of program
warnings – Warning control
traceback – Exception tracebacks

 
6. Memory & Performance
gc – Garbage collector
sys – Memory info, recursion limits


'''
# To see ALL built-in modules

help("modules")

#       or

import sys
print(sys.builtin_module_names)
```

```python
# Library

'''
A library in Python is a collection of pre-written code (modules, functions, and classes) 
that helps you perform tasks without writing code from scratch.

Libraries save time and effort.
You can import them into your program using import

'''

#  Custom / User-Defined Libraries

'''
Definition: Libraries created by yourself or someone else.
Purpose: Reuse code across multiple programs.
Example:
'''

# custom_library.py
def greet(name):
    return f"Hello, {name}!"

# main.py
from custom_library import greet
print(greet("Python"))
```

```python
#  Standard Library Modules 

'''
A standard library module is a module that comes bundled with Python. 
You don’t need to install it separately — it’s included with every Python installation.
just import and use them



1. Operating System and File Handling

os – Operating system interface
shutil – File operations like copy, move
glob – File pattern matching
pathlib – Object-oriented filesystem paths
fileinput – Iterate over lines from multiple input streams


2. Data Types and Data Handling

datetime – Dates and times
time – Time-related functions
calendar – Calendar operations
collections – Specialized data structures (deque, Counter)
array – Efficient arrays of basic types
heapq – Heap queue algorithms
bisect – Array bisection algorithms


3. Mathematical and Statistical

math – Basic math operations
cmath – Complex numbers
random – Random numbers
statistics – Statistical functions
fractions – Rational numbers
decimal – Decimal fixed-point and floating-point arithmetic


4. Text Processing

re – Regular expressions
string – Common string operations
textwrap – Text formatting
difflib – Comparing sequences


5. Data Persistence and Formats

json – JSON parsing and writing
csv – CSV files
configparser – INI file parsing
pickle – Object serialization
shelve – Persistent storage of objects


6. Networking and Internet

socket – Low-level network interface
http – HTTP clients and servers
urllib – URL handling
ftplib – FTP operations
email – Email handling


7. Program Execution and Debugging

sys – Interpreter info, command-line args
subprocess – Running external commands
logging – Logging messages
traceback – Error traceback
pdb – Debugger


8. Concurrency / Parallelism

threading – Threads
multiprocessing – Multi-process programs
asyncio – Asynchronous I/O
queue – Thread-safe queues


9. Cryptography and Security

hashlib – Hash functions
hmac – HMAC signatures
secrets – Secure random numbers


10. Other Utilities

argparse – Command-line argument parsing
timeit – Measuring execution time
functools – Higher-order functions
itertools – Efficient iterators
types – Dynamic type checking
warnings – Manage warnings

'''
```

```python
#  External / Third-Party Libraries

'''
Definition: Libraries not included with Python; must be installed via pip.
Purpose: Specialized tasks like data analysis, web development, machine learning.

Developed by external developers.
Must be installed using pip or another package manager.
Examples: numpy, pandas, requests, streamlit.

'''

# Various third party libraries that has common catagories 

'''
1. Data Manipulation & Analysis
NumPy – Numerical computations, arrays.
Pandas – Dataframes, CSV/Excel handling.
Openpyxl / xlrd – Excel file handling.


2. Data Visualization
Matplotlib – 2D plotting library.
Seaborn – Statistical plots built on Matplotlib.
Plotly (library mode) – Interactive charts (without Dash).
Bokeh – Interactive visualization.


3. Machine Learning & AI
Scikit-learn – ML algorithms.
XGBoost / LightGBM / CatBoost – Gradient boosting models.
TensorFlow (as library) – Low-level ML operations, tensor computation.
PyTorch (as library) – Neural networks, tensors.


4. Web & Networking Utilities
Requests – HTTP requests.
BeautifulSoup / lxml – Web scraping / parsing HTML.
Selenium – Browser automation.


5. File Handling & Compression
PyPDF2 / pdfminer – PDF reading/writing.
Pillow (PIL) – Image processing.
OpenCV – Computer vision and image processing.


6. Scientific & Math Libraries
SymPy – Symbolic mathematics.
SciPy – Scientific computations (integrals, optimization, etc.).
Statsmodels – Statistical modeling.


7. Utility Libraries
Click / argparse – Command-line interfaces.
Rich / Colorama – Styled terminal output.
Pydantic – Data validation and settings management.

'''
```

```python
# Framework

'''
A framework is a predefined structure or platform that helps developers build applications quickly by providing tools, templates, and reusable code.
Unlike a library, a framework calls your code (inversion of control).

Provides a skeleton for your application so you don’t have to handle everything manually.
Helps enforce best practices and organization in your project.

Key points:

Handles repetitive tasks like routing, database access, templates, or UI.
Can be web frameworks, GUI frameworks, or data/ML frameworks.

'''


# Popular Frameworks in Python

'''
1.  Web Frameworks
Django – Full-stack web framework, includes ORM, templates, authentication
Flask – Lightweight web framework, very flexible
FastAPI – Modern web framework for building APIs quickly
Bottle – Minimalist web framework


2.  GUI Frameworks
Tkinter – Built-in GUI toolkit for desktop apps
PyQt / PySide – Advanced GUI applications
Kivy – Cross-platform GUI for desktop and mobile


3. Data Science / ML Frameworks
Streamlit – Build interactive data apps quickly
Dash – Web apps for data visualization
TensorFlow – Deep learning framework
PyTorch – Machine learning and neural networks


4.  Game Development Frameworks
Pygame – 2D games development
Panda3D – 3D game engine

'''
```
