# Object Oriented Programming 

OOP is a programming paradigm which provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

## Classes

All object are instances of a class, which serves as the blueprint for an object type. 
Classes in python are used to create user defined data types. 

Class objects are instances of the class with actual values. 

### Instance Attributes 

Atrributes are also referred to as properties. 
The '__init__()' method is often used to initialize (e.g., specify) an object’s initial attributes by giving them their default value (or state). 

```
class Dog:

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

self refers to the individual instance of the class, and assigns values to the instances attributes. 

### Class Attributes 

While instance attributes are specific to each object, class attributes are the same for all instances.

```
class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The init is usally used to assign values to instance attributes. Instance methods can be used to modify the value of attributes based on some bheavior/action.

### Instantiating an Object 

```
# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Accessing the class attribiutes : Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))
```

### Instance Methods

They defined inside a class and are used to get the contents of an instance. They can also be used to perform operations with the attributes of our objects. Like the '__init__' method, the first argument is always self:

```
# instance method
    def send_email(self):
        self.is_sent = True
```

## Inheritance

One class takes the attributes of another class though inheritance. Child classes override or extend the functionality (e.g., attributes and behaviors) of parent classes. By default, Python 3 implicitly uses object as the parent class for all classes. So, 'class Dog:' is equivalent to writing 'class Dog(object):'.

- isinstance(\<obj\>, \<class\>) is used to determine if object \<obj\> is an instance of class \<class\>.

```
# Child class (inherits attributes and methods from the Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
```

Show examples of overriding, attributes/methods of the parent class. Extending attributes/method are quite simeple. What happens if one defines an init method in the child class. 


## Multiple Inheritance 

Unlike languages like Java and C#, python allows multiple inheritance i.e you can inherit from multiple classes at the same time like this:

```
class Subclass(SuperClass1, SuperClass2, ...):
   # initializer
   # methods
```

When one calls 'super().__init__()' what does it calL ? What happens when one uses methods that are present with the same name in different classes ? 

## Instance Methods vs Class Methods vs Static Methods 

```
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

- Instance Methods : The method takes one parameter, self, which points to an instance of the class. Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state. Instance methods can also access the class itself through the 'self.__class__' attribute.

- Class Methods : Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called. They can’t modify object instance state but only the class state. However, class methods can still modify class state that applies across all instances of the class. 

- Static Methods : They’re primarily a way to namespace your methods and can't access the class or the instance.

Look [here](https://realpython.com/instance-class-and-static-methods-demystified/) for more details. 

```
>>> obj = MyClass()
>>> obj.method()
# the above is just syntactic sugar for whats below.
>>> MyClass.method(obj)
```

Note : Please note that naming these parameters self and cls is just a convention. You could just as easily name them the\_object and the\_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.







