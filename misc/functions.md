# Functions in python 

Python’s functions are first-class objects. You can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions.

- Functions Can Be Passed To Other Functions(decorators)
- Functions Can Be Nested
- This means not only can functions accept behaviors through arguments but they can also return behaviors. 
- Functions Can Capture Local State

For some deatails look [here](https://dbader.org/blog/python-first-class-functions).

## main function 

Many programming languages have special functions that are executed as soon as the program is run. On the other hand, the Python interpreter executes scripts starting at the top of the file, and there is no specific function that Python automatically executes.

```
if __name__ == "__main__":
    do
```

It is set to the name of the module. In other words, for every module in your code, `__name__` will be set to that module name. And for the execution entry point, Python’s main script, the `__name__` variable will be set to `__main__`.

A nice explanation is given on [stack overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do?page=1&tab=votes#tab-top).

## Misc 

A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion. The order of keyword arguments doesn’t matter because Python knows where each value should go.

When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value. When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to con- tinue interpreting positional arguments correctly.

## Module

 A module is a file ending in .py that contains the code you want to import into your program. They are typically a bunch of functions. Each function within the module is accessible by `module_name.function_name()`. SPecific functions can also be imported from modules. 

- aliases : If the name of a function you’re importing might conflict with an exist- ing name in your program or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function. One can also guve aliases to modules. 
```
from pizza import make_pizza as mp
```

- importing all functions form a module `from pizza import *`. However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results. Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions.
The best approach is to import the function or functions you want, or import the entire module and use the dot notation. This leads to clear code that’s easy to read and understand.


