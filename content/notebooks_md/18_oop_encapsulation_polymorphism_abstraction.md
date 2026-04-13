# 18 - OOP - Encapsulation , Polymorphism., Abstraction

```python
# Encapsulation

'''Encapsulation is the concept of wrapping data (variables) and methods (functions) 
together into a single unit (class) and restricting direct access to some of the data.

| Type      | Syntax        | Meaning                                      |
| --------- | ------------- | -------------------------------------------- |
| Public    | `self.name`   | Accessible everywhere                        |
| Protected | `self._name`  | Should not be accessed directly (convention) |
| Private   | `self.__name` | Strongly restricted                          |
```

```python
#Mobile Phone Lock
class Mobile:
    def __init__(self):
        self.__password = "1234"

    def unlock(self, pwd):
        if pwd == self.__password:
            return "Phone Unlocked"
        else:
            return "Wrong Password"

m = Mobile()
print(m.unlock("1234"))
```

```python
# ATM Machine

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            return "Invalid PIN"

atm = ATM(1234, 5000)
print(atm.check_balance(1234))
```

```python
# Bank Account (Most Common Example)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())   # Balance is hidden and accessed only through methods.
```

```python
# Employee Salary System

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

    def get_salary(self):
        return self.__salary

emp = Employee(30000)
emp.set_salary(35000)
print(emp.get_salary())   # Employees cannot directly change their salary.
```

```python
# Polymorphism
# Polymorphism means “many forms”.
# it refers to the ability of a function, method, or operator to behave differently depending on the object or data type.
# Real time examples

''' As a teacher → teaches 📚
    As a parent → cares 👨‍👩‍👧
    As a friend → chats 😄

    In this example
    
    A person plays a multi roles '''

# python examples

class Student:
    def result(self):
        print("General result")

class SchoolStudent(Student):
    def result(self):
        print("School result")

class CollegeStudent(Student):
    def result(self):
        print("College result")

students = [SchoolStudent(), CollegeStudent()]

for s in students:
    s.result()
```

```python
# Method overloading or compile time polymorphism (Static Polymorphism)

''' 

Compile-time polymorphism is when the method to be executed is decided at compile time (before the program runs).

 How it works:
Achieved using method overloading
Same method name, but different:
number of parameters, or data types of parameters

for example

           In Other languages like java                                       |              In python language
                                                                              |
--> we need to mention the datatype what we are given                         | we dont need to mention the datatype what we are given
inside and outside of a function because it use static typing                 |  inside and outside of a function because it use dynamic typing
                                                                              |
--> Static typing means the type of a variable is known at                    | Dynamic typing means the type of a variable is decided at runtime, 
compile time and must be declared in advance.                                 |  and you don’t need to declare it explicitly.
                                                                              | 
Key points:                                                                   | Key points:
You must specify the data type                                                |  No need to specify data type
Type checking happens before execution                                        |  Type checking happens during execution
Errors are caught early (at compile time)                                     |  More flexible, but errors can occur at runtime
                                                                              |
                                                                              | Python simulates compile-time polymorphism using:
                                                                              | Default arguments default = 0 (a,b,c=0) this is used by 
                                                                              |  knowing the incoming of no of inputs
                                                                              |  Variable-length arguments (*args) this is used by
                                                                              |   unknowing the incoming of no of inputs 
                                                                              |  Type checking inside functions
class Summation:                                                              |
         int sum(int a,int b)                                                 |class Summation:
             return a+b                                                       |        def sum(self,*args):
         float sum(float a,float b)                                           |             ans = 0
               return a+b                                                     |             for i in args:   
         int sum(int a,int b,int c)                                           |                 ans += 1
             return a+b                                                       |              return ans
                                                                              |
sum(12,12) -----> calls out the first int function                            |summation = Summation()
sum(13.0,12.9) -----> calls out the second float function                     |print(sumation.sum(1,2,3,4,etc....))
sum(23,33,44)--------> calls out the third function which has three arguments |
                                                                              | we can pass n number of values in this case by using *args
                                                                              | it returns the solved values of all values by what we declaring.

Method Signature (refined):
A method signature refers to a method having the same name but differing in the number of parameters or the data types of its parameters.

Method Binding (refined):
Method binding is the process where, when a method is called, the compiler determines and links the call to the correct method 
implementation based on the method signature.
```

```python
# Method overriding or Run-Time Polymorphism (Dynamic Polymorphism)

''' Run-time polymorphism is when the method to be executed is decided at runtime (while the program is running).

How it works:
Achieved using method overriding
A subclass provides a specific implementation of 
a method already defined in the parent class

for example
                     In Other languages like java         |                In python language            
                                                          |
                                                          |
class Animal                                              |class Father:
    void sound() {                                        |    def __init__(self):
        System.out.println("Animal makes sound");         |        print("Father Constructor")
    }                                                     |    def say_hello(self):
}                                                         |         print("say hello from father")
                                                          |
class Dog extends Animal {                                |class Child:
    void sound() {                                        |     def__init__(self):
        System.out.println("Dog barks");                  |         print("Child Constructor")
    }                                                     |     def say_hello(self):
}                                                         |         print("say hello from child")
                                                          |
Animal a = new Dog();                                     | child = Child()
a.sound();  // Calls Dog's method                         | child.say_hello  // calls child`s method
```

```python
# Method Overriding (Inheritance Based Polymorphism)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat()]

for a in animals:
    a.sound()
```

```python
# Using super() with Polymorphism
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()
```

```python
# Duck Typing (Python-style Polymorphism)
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def make_fly(obj):
    obj.fly()

make_fly(Bird())
make_fly(Airplane())
```

```python
# Payment System (Different Payment Methods)

class Payment:
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

# Polymorphism in action
payments = [CreditCardPayment(), PayPalPayment(), UpiPayment()]

for p in payments:
    p.pay(1000)             # A system can process Credit Card, PayPal, or UPI payments using the same method name pay()
```

```python
# Shape Area Calculation


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]  

for s in shapes:
    print(s.area())   # Different shapes calculate area differently, but we call the same method area().
```

```python
# Abstraction
# Hiding implementation details and showing only essential features.
# Abstraction means defining a common interface in the parent class and hiding the implementation details, which are provided by the child classes.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
d = Dog()
c = Cat()

d.sound()
c.sound()
```

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


payments = [CreditCard(), UPI()]

for p in payments:
    p.pay(1000)
```

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name 

    @abstractmethod
    def go(self):
        pass

    @abstractmethod    
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print(f"You start the car {self.name}")

    def stop(self):
        print(f"You stop the car {self.name}")

class Motorcycle(Vehicle):
    def go(self):
        print(f"you start the Motorcycle {self.name}")
    def stop(self):
        print(f"you stop the Motorcycle {self.name}")  


class Boat(Vehicle):
    def go(self):
        print(f"you Sail the Boat {self.name}")
    def stop(self):
        print(f"you anchor the Boat {self.name}")      


car = Car("Herby")
car.go()
car.stop()

motorcycle = Motorcycle("Yamaha")
motorcycle.go()
motorcycle.stop()

boat = Boat("Black pearl")
boat.go()
boat.stop()
```
