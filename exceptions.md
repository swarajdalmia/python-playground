# Exceptions

Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python unsure what to do next, it creates an exception object. One can either deal with them, if not, the program will halt and show a traceback, which includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. 

## try-except blocks

```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.

Exceptions are used to prevent crashes. 


