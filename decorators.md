# Decorators 

By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

## Functions as First-class Objects

In Python,functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object.

```
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
```

Now, one can perform the call shown below:
```
>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
```

The be\_awesome function is named without parentheses. This means that only a reference to the function is passed. The function is not executed. The greet\_bob() function, on the other hand, is written with parentheses, so it will be called as usual.

## Inner Functions

It’s possible to define functions inside other functions. Such functions are called inner functions.

```
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
```

On executing parent(), the output is:
```
parent()
Printing from the parent() function
Printing from the second_child() function
```
The order in which the inner functions are defined does not matter. The printing only happens when the inner functions are executed. The inner functions are not defined until the parent function is called. They are locally scoped to parent() i.e. they only exist inside the parent() function as local variables.

Python also allows you to use functions as return values, by returning the function name without the paranthesis. 

## Simple Decorators : Around functions

Decorators wrap a function, modifying its behavior as shown below.

```
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# the decoration happens at the following line
say_whee = my_decorator(say_whee)
```
The above definition seems a bit clunky and python helps simplify that with @decorator. 
The code bwlow, does the same thing as above. 

```
def my_decorator(func):
    def wrapper():
        @functools.wraps(func)  # helps keep the information about the function, same as the function and not as equal to the wrapper
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

**Decorating Functions with Arguments** : The solution is to use \*args and \*\*kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments. See example [here](https://realpython.com/primer-on-python-decorators/).

- In case the function around which one is decorating is returning a value we need to add a return with \*args and \*\*kwargs in the wrapper decorator. 
- The @functools.wraps decorator uses the function functools.update\_wrapper() to update special attributes like __name__ and __doc__ that are used in the introspection.


### Template 

```
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

## Example Decorators 

- to calculate the time taken a function to execute. [here](https://realpython.com/primer-on-python-decorators/)
- a decorator to slow down a function by 1 second.
- login required before executing something


## More Complex Decorators Applications

Decorating classes:
- it is possible to decorate the entire class. One dynamically changes a class defn, and it can be used instead of meta classes.

Nesting Decorators:
- One can apply several decorators to a function by stacking them on top of one another. 

One can also pass arguments to the decorator. Decorator args, function args can be seperated. 
- One can also define decorators that can be used both with and without arguments 

Stateful Decorators:
- a decorator that can keep track of state by using function attributes, func\_name.var\_name. However, the typical way to maintain state is by using classes. Examples of using both are shown in the tutorial. 

Decorators can provide a nice mechanism for caching and memoization.
- In the standard library, a Least Recently Used (LRU) cache is available as @functools.lru\_cache which one can use.


