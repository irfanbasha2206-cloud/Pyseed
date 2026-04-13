# 19 - OOP - Inheritance

```python
#inheritance

'''Inheritance in Python is a concept where one class (child/subclass) gets the properties and methods of another class (parent/superclass). 
It helps you reuse code and build relationships between classes.'''

# Types of inheritance
''' single inheritance
    multiple inheritance
    multilevel inheritance
    hierarchical inheritance 
    hybrid inheritance'''
```

```python
# Single inheritance means One child class inherits or deriving properties from one parent class.
# example

class parent:
    def f1(self):
        print("f1 from parent class")
    def f2(self):
        print("f2 from parent class")

class child(parent):
    def f3(self):
        print("f3 from child class")
    def f4(self):
        print("f4 from child class")

obj = child()   # object created for child class
obj.f1()        # but calling the parent class properties it works by child inherited by parent
```

```python
# Multiple inheritance means One child class inherits from multiple parent class.
# example    

class father:
    def f1(self):
        print("f1 from father class")
    def f2(self):
        print("f2 from father class")

class mom:
    def f3(self):
        print("f3 from mom class")
    def f4(self):
        print("f4 from mom class")

class child(father,mom):
    def f5(self):
        print("f5 from child class")
    def f6(self):
        print("f6 from child class")
```

```python
obj = child()  # created object for child calss
obj.f2()        # calling the property of greatgrandfather class while we inherit in childclass
```

```python
obj.f4()
```

```python
obj.f5()
```

```python
obj.f7()
```

```python
# if we use same methods in different classes the order to be starts with child class then parent 1 --> parent 2 -->......
# to know the order of inheritance
# childclassname.__mro__
```

```python
# Method overiding concept 
# if parent and child class use same method but different behaviour 
# for example

class father:
    def f1(self):
        print("f1 from father class")
    def f2(self):
        print("f2 from father class")

class mom:
    def f1(self):
        print("f1 from mom class")
    def f4(self):
        print("f4 from mom class")

class child(father,mom):
    def f1(self):
        print("f1 from child class")
    def f6(self):
        print("f6 from child class")
```

```python
obj = child()
obj.f1()   # f1 method is used in two different classes but it follows the order by rule of first child class
            # if child class does not have that method it follows what we have inherit in child class at first to last flow
```

```python
child.__mro__
```

```python
# Multilevel Inheritance means A chain of inheritance. A 1st parent class properties is uses by 2nd parent class and also a child class.
#for example

class greatgrandfather:
    def f1(self):
        print("f1 from greatgrandfather class")
    def f2(self):
        print("f2 from greatgrandfather class")

class grandfather(greatgrandfather):
    def f3(self):
        print("f3 from grandfather class")
    def f4(self):
        print("f4 from grandfather class")

class father(grandfather):
    def f5(self):
        print("f5 from father class")
    def f6(self):
        print("f6 from father class")

class child(father):
    def f7(self):
        print("f7 from child class")
    def f8(self):
        print("f8 from child class")
```

```python
obj = child()
obj.f7()
```

```python
obj.f6()
```

```python
obj.f4()
```

```python
obj.f2()
```

```python
class Grandpa:
    def phone(self):
        print("Grandpa phone")

class Dad(Grandpa):
    def money(self):
        print("Dad`s Money")

class Son(Dad):
    def laptop(self):
        print("Son`s Laptop")

irfan = Son()
irfan.money()
irfan.phone()
```

```python
# Hierarchical Inheritance means Multiple child classes inherit from the same parent class.

class parent:
    def f1(self):
        print("f1 from parent class")
    def f2(self):
        print("f2 from parent class")

class child1(parent):
    def f3(self):
        print("f3 from child 1 class")
    def f4(self):
        print("f4 from child 1 class")

class child2(parent):
    def f5(self):
        print("f5 from child 2 class")
    def f6(self):
        print("f6 from child 2 class")

class child3(parent):
    def f7(self):
        print("f7 from child 3 class")
    def f8(self):
        print("f8 from child 3 class")
```

```python
obj = child1()
obj.f1()
```

```python
obj = child2()
obj.f1()
```

```python
obj = child3()
obj.f1()
```

```python
# Hybrid Inheritance means A combination of two or more types of inheritance.
class parent:
    def f1(self):
        print("f1 from parent class")
    def f2(self):
        print("f2 from parent class")

class child1(parent):
    def f3(self):
        print("f3 from child 1 class")
    def f4(self):
        print("f4 from child 1 class")

class child2(parent):                  # here Hierarchical inheritance is used
    def f5(self):
        print("f5 from child 2 class")
    def f6(self):
        print("f6 from child 2 class")

class child3(child1,child2,parent):   # here multiple inheritance is used 
    def f7(self):
        print("f7 from child 3 class")
    def f8(self):
        print("f8 from child 3 class")
```

```python
obj = child3()   # creating a object for chlild 3
obj.f3()   # accessing the property of child 1 from chlild 3     -----> multiple inheritance is used
```

```python
obj.f5()  # accessing the property of child 2    -----> multiple inheritance is used
```

```python
obj.f2() # accessing the property of parent   -----> multiple inheritance is used
```

```python
obj = child2()
obj.f1()  # accessing the property of parent class by child 2   --------> Hierarchical inheritance is used
```

```python
obj = child1()
obj.f1()    #  accessing the property of parent class by child 1    --------> Hierarchical inheritance is used
```

```python
# super function
# super() is used in a child class to call or modify methods from a parent class (super class).
# Allows you to extend the functionality of the inherited methods.
# super() is mainly used in in Inheritance

class Shape:
    def __init__(self,shape,color,is_filled):
        self.color = color
        self.is_filled  = is_filled
        self.shape = shape
    def describe(self):
        print(f"{self.shape} is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class Circle(Shape):
    def __init__(self,shape,color,is_filled,radius):
        super().__init__(shape,color,is_filled)                    # super() refers to --> parent classname (Shape)
        self.radius = radius
        
class Square(Shape):
    def __init__(self,shape,color,is_filled,width):
        super().__init__(shape,color,is_filled)                    # super() refers to --> parent classname (Shape)
        self.width = width
        
class Triangle(Shape):
    def __init__(self,shape,color,is_filled,width,height):
        super().__init__(shape,color,is_filled)                    # super() refers to --> parent classname (Shape) 
        self.width = width
        self.height = height

circle = Circle("Circle","Red" , True , 5)
square = Square("Square","Blue" , False , 8)
triangle = Triangle("Triangle","Black",True, 4,6)

print("Shape = ",circle.shape,"\nColor = ", circle.color,"\nIs_filled =", circle.is_filled , "\nRadius =", circle.radius ,"Cm",)
circle.describe()
print()

print("Shape = ",square.shape,"\nColor = ", square.color,"\nIs_filled =", square.is_filled , "\nWidth =",square.width,"Cm")
square.describe()
print()

print("Shape = ",triangle.shape,"\nColor = ", triangle.color,"\nIs_filled =", triangle.is_filled , "\nWidth =",triangle.width,"Cm", "\nHeight =",triangle.height,"CM")
triangle.describe()
```

```python
# super() in simple
class Cat:
    def __init__(self):
        print("I Love Fish")
        print("I Love Milk")

class Rat(Cat):
    def __init__(self):
        super().__init__()
        print("I Love Cheese")

jerry = Rat()
```

```python
# using super function in method overiding to extend the methods

class Shape:
    def __init__(self,shape,color,is_filled):
        self.color = color
        self.is_filled  = is_filled
        self.shape = shape
    def describe(self):
        print(f"{self.shape} is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class Circle(Shape):
    def __init__(self,shape,color,is_filled,radius):
        super().__init__(shape,color,is_filled)                    
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is {self.shape} with the area of {3.14 * self.radius*self.radius}cm^2")
        
        
circle = Circle("Circle","Red" , True , 5)
circle.describe()
```

# Brief explain of types of inheritance

```python
'''Simple tables of Inheritances
| Type         | Description                  |
| ------------ | ---------------------------- |
| Single       | One parent → one child       |
| Multiple     | Multiple parents → one child |
| Multilevel   | Chain of inheritance         |
| Hierarchical | One parent → many children   |
| Hybrid       | Combination of above types   |
```

```python
# 1. Single Inheritance

# One child contains one parent class.

class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

obj = B()
obj.show()
obj.display()
```

```python
# 2. Multiple Inheritance

# One child class contains many parent class.

class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):
    def print_data(self):
        print("Class C")

obj = C()
obj.show()
obj.display()
```

```python
# 3. Multilevel Inheritance

# A chain of inheritance (grandparent → parent → child).

class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def print_data(self):
        print("Class C")

obj = C()
obj.show()
obj.display()
```

```python
# 4. Hierarchical Inheritance

# Multiple child classes contains same parent class.

class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

b.show()
c.show()
```

```python
# 5. Hybrid Inheritance

# A combination of two or more types of inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()
```
