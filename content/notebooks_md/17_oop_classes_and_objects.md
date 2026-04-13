# 17 -  OOP - Classes and Objects

```python
# OOP
''' OOP (Object-Oriented Programming) in Python is a way of writing code by organizing it into objects instead of just functions and variables.

In real world we can`t do projects with procedural programming like using functions and variables.

for example :-

 1st car
          a = car                                   |                                      
          no_of_wheels  = 4                         |
          no_of_airbags = 2                         |
           gears        = 5                         |        CARS ----> OBJECT 
          seats         = 6                         |        PROPERTIES OF CARS (VARIABLES)----> WHEELS , AIRBAGS , GEARS AND SEATS
          speed         = 110                       |        BEHAVIOUR OF PROPERTIES (FUNCTION) ----> moveforward , backforward
                                                    |
                                                    |
def moveforward():                                  |         
         print("Car is moving forward",speed)       |
def backforward():                                  |
         print("Car is moving backward",speed-100)  |
                                                    |  
2nd car                                             |           
          a_2 = 2_car                               |    SIMILARLY WE HAVE TO CREATE 2ND CAR VARIABLES AND DECLARE NEW VARIABLE NAMES FOR THE
          no_of_wheels_2  = 5                       |    PROPERTIES AND AS WELL AS NEW FUNCTION NAMES FOR CLEAR UNDERSTANDING WHICH CAR IS 
          no_of_airbags_2= 5                        |    MOVING IN WHICH SPEED
          gears_2        = 6                        |
          seats_2        = 4                        |  
          speed_2         = 130                     |    
                                                    |    
def moveforward2():                                 |         
         print("Car is moving forward",speed)       |
def backforward2():                                 |
         print("Car is moving backward",speed-100)  |
                                                    |

--> In real time there is lakhs of cars and we can`t create thousands of variables and functions separately using procedural 
    programming.

--> But in object oriented programming we can do

for example:=

class Car:
      wheels = 4
      gears = 5                 # class is created for car and what are all inside the class we collectively called as data members.
      airbags = 4
      seats = 6                        # inside the class , variables are called as attributes and functions are called as methods
      def moveforward(self):                                        
          print("Car is moving forward",speed)    # specify the self inside def function parameter is to pass the 
      def backforward(self):                               object itself as a 1st argument   
          print("Car is moving backward",speed-100)

car1 = Car()                                            # here object is created for Car class that is called instance of a class
car2 = Car()                                               #  we called this process Instantiation
car2.wheels = 6

# to call the variable inside the class use objectname.variablename

print(car1.wheels)
print(car2.wheels)

output of car1 will be ---> 4          # there will be changes in car1           
output of car2 will be ---> 6          # it is only changed in car2


# to call the function inside the class use objectname.functionname
print(car1.moveforward)

output of car1 will be ----> Car is moving


# Main concepts of oops
''' # classes and objects
    # inheritance
    # polymorphism
    # encapsulation
    # abstraction '''
```

```python
# classes and objects
# class
''' class is a blueprint for creating objects
    It defines properties (attributes) like variables and behaviors (methods) like def function.
    Attributes are variables inside a class that store data about an object.
    Methods are functions defined inside a class that describe what an object can do.
    It is used mainly built software application.'''


# real time example with instagram 

'''
                                                              class
                                                            (Instagram)     
                                                                |
                                                                |
                                                    ---------------------------
                                                    |           |             |
                                                  (user_1)    (user_2)     (user_3)
                                                  object_1    object_2     object_3      '''

#class snytax ---> class Name:
# name starts with capital letter its not rule but it is followed.  
#to access the variable inside the class with class name.variable name
#example

class Student:
    name = "Irfan"
    age = 24
    language = "python"

print(Student.name)
```

```python
# to update the class variable 
class Student:
    name = "Irfan"
    age = 24
    language = "python"

Student.name = "basha"
Student.name
```

```python
#to update and see the variable inside the class  
# to update -->  classname.variablename = "updated name"
# to see use --> classname.__dict__
#for example
class Student:
    name = "Irfan"
    age = 24
    language = "python"

Student.name = "basha"
Student.__dict__
```

```python
# to add the new variable inside the class when class already created use classname.newvariable = "new variable value"
class Student:
    name = "Irfan"
    age = 24
    language = "python"

Student.mobile = 8939660877
Student.mobile
```

```python
# to access the method used inside the class
class Student:
    name = "Irfan"
    age = 24
    language = "python"
    def check():
        print("Hi",Student.name,"your age is",Student.age)   # when class variable used in class method use class name inside the class method

Student.check()    # to call class method use class name.method name()
```

```python
# object
'''An object is an instance of a class.
   It is the actual implementation of the class.
   Each object can have its own data.
   It is to create a variable for class
   n number of objects can be created for a class
   we can update the variable value by object'''

class Student:
    name = "Irfan"
    age = 24
    language = "python"

obj1 = Student
obj1.name
```

```python
obj2 = Student
obj2.__dict__
```

```python
# to update the variable value by object

obj3 = Student
obj3.language = "c++"
obj3.language
```

```python
#to see the updated variable inside the object use (objname.__dict__)
obj3.language
obj3.__dict__
```

```python
# initializer or init
# it is a magic method because it calls itself when we create an object for a class by using it.
# when class was created there would be a constant empty init method at first. 
# when we use the init method to define some variables or built_in function under init the empty get some values.
# for example

class Demo:
    def __init__(self):
        print("Hello")
        print("Python")
        a = 10
        b = 20
        c = a + b
        print(c)
    def check(self):
        print("java")
        print("google")
        print("c++")

obj1 = Demo()    # here we cant call the init method by object just created a oject for class
```

```python
# Types of variables
# class variable vs instance variable (object)

'''              class variable                                     |                             instance variable
                                                                    |              
    class variable is to access , update ,add or delete or any      |  instance variable  is to ,access , update ,add or delete or any other changes
    changes by using direct variables inside under the class        |   by using init method.
     and defined outside of init method it is accessed by           |
     classname and also object name.                                |  --> Accessing by classname it shows some memory address because it is not                 
                                                                    |      stored  in a variable, Python automatically prints the returned  
                                                                    |      object in some environments (like interactive shell / REPL / IDLE).
                                                                    |
                                                                    | --> Acessing by objectname it won`t show any address because The object is now 
                                                                    |     stored in variable created by You. Python does not automatically print it.
                                                                    |   
                                                                    |
class Student:                                                      |  class Student:
                                                                    |        def __init__(self,name,age,language):
    name = "Irfan"                                                  |            self.name = name         
    age = 24                                                        |            self.age = age 
    language = "python"                                             |            self.language = language
                                                                    |
Student.name  ---->  accessing by classname                         | obj = Student("Irfan",24,"python") ----> passing values through the constructor
obj = Student     ----> creating object                             |       
obj.name          ----->  accessing by objectname                   |  
                                                                    |
                                                                    |
                                                                    |
```

```python
# class variable and instance variable simple connection
# class variable is to store common default values
# instance varible is to store unique different values

class Phone:
    chargertype = "C-type"
    def __init__(self,brand,price,camera):
        self.brand = brand
        self.price = price
        self.camera = camera
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("Chargertype : ",self.chargertype)    # either we use Phone.chargertype or self.chargertype for a class variable
                                                      # if Phone.chargertype is used later there would be a possibilities to add or change of values
apple = Phone("Apple",80000,"70mp")                        # it would affects the other objects also
apple.chargertype = "Wireless , C-type" 
apple.display()                                        # but if we use self the current object instance changes it current value and it not
print()                                                  # affect the other objects
                                                       
vivo = Phone("Vivo",40000,"50mp")
vivo.display()
print()

moto = Phone("Motorola",20000,"30mp")
moto.display()
```

```python
# class variable and instance variable complex connection
class Student:
    class_year = 2026
    num_students = 0
    subjects = 5

    def __init__(self, name, mark, grade):
        self.name = name
        self.mark = mark
        self.grade = grade
        Student.num_students += 1


student1 = Student("James cameron", 78, "A")
student2 = Student("Mark zuckerbherg", 88, "A+")

print("My graduating class of" , (Student.class_year), "has" , (Student.num_students), "Students")
print()

print("Student1:", student1.name)
print("Mark:", student1.mark)
print("Grade:", student1.grade)
print("Student class year:", student1.class_year)    # ----> accessing the class_variable by object_name
print("No of Subjects:", Student.subjects)
print()


print("Student2:", student2.name)
print("Mark:", student2.mark)
print("Grade:", student2.grade)
print("Student class year:", Student.class_year)    # ----> accessing the class_variable by class_name for clear readibilty to explicit using
print("No of Subjects:", Student.subjects)
```

```python
# Types of methods

# 1 Instance Method
# Works with object (instance) data

'''Uses self
Can access instance variables and class variables
Example:'''

class Phone:
    chargertype = "C-type"

    def __init__(self, brand):
        self.brand = brand

    def show(self):   # instance method
        print("Brand:", self.brand)
        print("Charger:", self.chargertype)

p1 = Phone("Apple")
p1.show()
```

```python
# 2 Class Method
# Works with class-level data

'''Uses cls
Can access only class variables
Defined using @classmethod
Example:'''

class Phone:
    chargertype = "C-type"

    @classmethod
    def change_charger(cls, new_type):
        cls.chargertype = new_type

Phone.change_charger("Wireless")
print(Phone.chargertype)
```

```python
# 3 Static Method
# Does not depend on class or object

'''No self or cls
Defined using @staticmethod
Works like a normal function but belongs to a class
Example:'''

class Phone:

    @staticmethod
    def info():
        print("Phones are electronic devices")

Phone.info()
```

```python
# @ decorator
# @ is a shortcut syntax used to apply a decorator to a function or method.
# Instead of modifying a function directly, you "wrap" it using another function.

#Basic Example (without @)

class Phone:
    def __init__(self, brand):
        self.brand = brand

    def show(self):   # instance method
        print("Brand:", self.brand)

p1 = Phone("Apple")
p1.show()
```

```python
#Same Example (with @)

class Phone:
    chargertype = "C-type"

    @classmethod
    def change_charger(cls, new_type):
        cls.chargertype = new_type

# call using class
Phone.change_charger("Wireless")

print(Phone.chargertype)
```

```python
# Mini bank statement
class Bank:
    def deposit(obj,amount):
        obj.balance += amount
    def balance_enquiry(obj):
        print(obj.name,"your bank balance amount",obj.balance)
```

```python
c1 = Bank()
c1.name = "Irfan"
c1.accno = 6002
c1.balance = 1000
c1.__dict__
```

```python
#to access the class methods by calling classname.methodname()

Bank.deposit(c1,4000)  # 1000 balance is already having in c1 bank 4000 to be deposited so it adds balance + deposited amount
c1.__dict__
```

```python
Bank.balance_enquiry(c1)
```

```python
c2 = Bank()
c2.name = "basha"
c2.accno = 6005
c2.balance = 3000
c2.__dict__
```

```python
Bank.deposit(c2,6000)
c2.__dict__
```

```python
Bank.balance_enquiry(c2)
```

```python
class Bank:
    def deposit(self,amount):
        self.balance += amount
    def balance_enquiry(self):
        print(self.name,"your bank balance amount",self.balance)
```

```python
#to access the class methods by calling objectname.methodname()
c3 = Bank()
c3.name = "Besant"
c3.balance = 2000
```

```python
c4  = Bank()
c4.name = "Tech"
c4.balance = 3000
```

```python
# by calling with object it would take the object has first or self argument no need to pass the object inside the parameters
c3.deposit(2000)
c3.__dict__
```

```python
c3.balance_enquiry()  # no need to pass any argument inside the parameter because c3 the object itself passing it as a argument inside the parameter
```

```python
c4.deposit(3000)
c4.__dict__
```

```python
c4.balance_enquiry()
```

```python
obj1.check()
```

```python
class Bank:
    def __init__(self,username,useraccno,userbalance):
        self.name = username
        self.accno = useraccno
        self.balance = userbalance
    def deposit(self,amount):
        self.balance += amount
    def balance_enquiry(self):
        print(self.name,"your bank balance amount",self.balance)
```

```python
c1 = Bank("Irfan",60980,20000)
c1.__dict__
```

```python
c2 = Bank("basha",45778,10000)
c2.__dict__
```

```python
c1.deposit(2000)
c1.balance_enquiry()
```

```python
c2.deposit(4000)
c2.balance_enquiry()
```

```python
# Library management

class Library:
    def __init__(self, booklist):
        self.books = booklist

    def display(self):
        print("\nAvailable books are:")
        for book in self.books:
            print("-", book)

    def borrow_book(self):
        bookname = input("Enter the book name you want to borrow: ")
        if bookname in self.books:
            self.books.remove(bookname)
            print(f"You have borrowed '{bookname}'")
        else:
            print("Sorry! Book not available.")

    def return_book(self):
        bookname = input("Enter the book name you want to return: ")
        if bookname in self.books:
            print("This book is already in the library.")
        else:
            self.books.append(bookname)
            print(f"Thanks for returning '{bookname}'")
```

```python
li = ["python", "java", "c++" , "C#" , "html"]
obj = Library(li) 
obj.__dict__
```

```python
obj.display()
```

```python
obj.borrow_book()
```

```python
obj.return_book()
```

```python
class Student:
    def __init__(self,name,age,language):
        self.name = name
        self.age = age 
        self.language = language
        
obj = Student("Irfan",24,"python")
print(obj.name)
```
