## Python features 
- Python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters, functions, or methods in source code. This makes the code short and flexible, and you lose the compile-time type checking of the source code. Python tracks the types of all values at runtime and flags code that does not make sense as it runs.

- The end of a line marks the end of a statement, so no need for semicolons.

- Comments begin with "#"

- Python source files use the ".py" extension and are called "modules."

- When a Python file is run directly, the special variable "\_\_name\_\_" is set to "\_\_main\_\_". Therefore, it's common to have the boilerplate if \_\_name\_\_ ==... shown above to call a main() function when the module is run directly, but not when the module is imported by some other module.

- In a standard Python program, the list sys.argv contains the command-line arguments in the standard way with sys.argv[0] being the program itself, sys.argv[1] the first argument, and so on. If you know about argc, or the number of arguments, you can simply request this value from Python with len(sys.argv).



A lot of these are taken form [here](https://developers.google.com/edu/python/introduction).
