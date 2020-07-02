# Documenting Python Code

```
“Code is more often read than written.”

— Guido van Rossum
```

When you write code, you write it for two primary audiences: your users and your developers (including yourself). I’m sure you’ve run into a situation where you wanted to do something in Python and found what looks like a great library that can get the job done. However, when you start using the library, you look for examples, write-ups, or even official documentation on how to do something specific and can’t immediately find the solution.

```
“It doesn’t matter how good your software is, because if the documentation is not good enough, people will not use it.“

— Daniele Procida
```

## Commenting vs. Documenting Code

In general, commenting is describing your code to/for developers. In conjunction with well-written code, comments help to guide the reader to better understand your code and its purpose and design. 

Documenting code is describing its use and functionality to your users. While it may be helpful in the development process, the main intended audience is the users.

## Commenting 

According to PEP 8, comments should have a maximum length of 72 characters. 
Purpose of commenting:

- Planning and Reviewing: When you are developing new portions of your code, it may be appropriate to first use comments as a way of planning or outlining that section of code. Remember to remove these comments once the actual coding has been implemented and reviewed/tested.
```
# First step
# Second step
# Third step
```

- Code Description: Comments can be used to explain the intent of specific sections of code.

- Algorithmic Description: When algorithms are used, especially complicated ones, it can be useful to explain how the algorithm works or how it’s implemented within your code. It may also be appropriate to describe why a specific algorithm was selected over another.

- Tagging: The use of tagging can be used to label specific sections of code where known issues or areas of improvement are located. Some examples are: BUG, FIXME, and TODO.

Note: Design your code to comment itself. The easiest way to understand code is by reading it. When you design your code using clear, easy-to-understand concepts, the reader will be able to quickly conceptualize your intent.

## Commenting Code via Type Hinting 

Type hinting was added to Python 3.5 and is an additional form to help the readers of your code. It allows the developer to design and explain portions of their code without commenting. Here’s a quick example:

```
def hello_name(name: str) -> str:
    return(f"Hello {name}")
```

## Documenting with docstrings

### Background 

Documenting your Python code is all centered on docstrings. These are built-in strings that, when configured correctly, can help your users and yourself with your project’s documentation. Along with docstrings, Python also has the built-in function help() that prints out the objects docstring to the console. 

### Docstring Types 

- Class Docstrings: Class and class methods
- Package and Module Docstrings: Package, modules, and functions
- Script Docstrings: Script and functions

For conventions and what to include for each look [here](https://realpython.com/documenting-python-code/).


### Docstring Formats

Google, reStruc, Numpy, Epytext. 

For more resources and tools on documentation look [here](https://realpython.com/documenting-python-code/).  Come back to this again !


