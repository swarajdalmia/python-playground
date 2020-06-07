# Assert

The assert statement is a debugging aid that tests a condition. If the assert condition is true, nothing happens, and your program continues to execute as normal. But if the condition evalu- ates to false, an AssertionError exception is raised with an optional error message.

An example:
```
assert 0 <= price <= product['price']
```
The above is used to assert that the price after discount is withing a certain range. 

## When to use assert ?

Now, why does one need 'assert' when one can use if else ?
- One should usually asserts only in cases of unrecoverable errors in a program.
- Asserts are meant to insure internal self-checks for the programs.
- Assertions are not intended to signal expected error conditions, like a File-Not-Found error, where a user can take corrective actions or just try again.
- Aeerts are not meant to handle run-time errors, rather assist in debugging.

For now, keep in mind that Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors and asserts should never be raised unless there is a bug in the program.

## Syntax 

```
assert test_expression [, error_message]
```

Unwrapping the actual workings, something like the following is executed:
```
if __debug__:
    if not test_expression:
        raise AssertionError(error_message)
```
The working of all asserts can be disabled, with the -O and -OO command line switches, as well as the PYTHONOPTIMIZE environment variable in CPython, hence if some checks are done with assert, and since they can be turned off, it might cause issues. 

Rules of thumb:
- The answer is to never use as- sertions to do data validation. Instead, we could do our validation with regular if-statements and raise validation exceptions if necessary.
- Asserts that never fail : When you pass a tuple as the first argument in an assert statement, the assertion always evaluates as true and therefore never fails.

