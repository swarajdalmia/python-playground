# Classes in Python

Apart from other reasons, classes are a way to implement OOP concepts. 

## The init() method

A function that’s part of a class is a method. The __init__() method atwis a special method Python runs automatically whenever we create a new instance of a class. 

The self parameter is required in the method definition, and it must come first before the other parameters. It must be included in the def- inition because when Python calls this __init__() method later (to create an instance of Dog), the method call will automatically pass the self argument.

```
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
```
### Creating an instance

```
class Dog(): 
    --snip--

my_dog = Dog('willie', 6)
```

The __init__() method has no explicit return statement, but Python automatically returns an instance representing this dog. 

- accesing attributes: this is done by using the dot notation.
 
## Inheritance 

You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The child class inherits every attribute and method from its parent class but is also free to define new attributes and methods of its own.

### init for a child class

A class in inherited by placing the name of the parent class in the braces while declaring the child class. The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class. To do this, the __init__() method for a child class needs help from its parent class.

The super() function is a special function that helps Python make connections between the parent and child class. It tells Python to call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class. The attributes for the child class can be declared in the init after calling super.
 
```
class Car():
"""A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
"""Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        x super().__init__(make, model, year)
```

### Over-riding methods from the parent class

To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

### Instances as Attributes

When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together and use the instace of another class as an attribute of a different class. [look at page 175 from the python crash course book for example].

## Importing classes

As you add more functionality to your classes, your files can get long, even when you use inheritance properly. To help, Python lets you store classes in modules and then import the classes you need into your main program.

The import statement can be used to import a specific class from a specific module. A module can simply be the name of a .py file containing a class. You can store as many classes as you need in a single module, although each class in a module should be related somehow. One can import an entire class(one then has to use . to access the different classes), one can specifically import some classes or import all classes using \*. 

## the Python standard library

The Python standard library is a set of modules included with every Python installation. Though the modules are installed they still need to be imported. A module is simply a pythin file. 

How to get a list of all the modules included as part of an installation. There is no one command which gives such a list. However, one can find the list [here](https://docs.python.org/3/library/index.html).

 
