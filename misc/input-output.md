# Input, Output and command line interface

## Input 

`input()` pauses program execution to allow the user to type in a line of input from the keyboard. Once the user presses the Enter key, all characters typed are read and returned as a string. If you include the optional <prompt> argument, input() displays it as a prompt to the user before pausing to read input:

```
>>> name = input('What is your name? ')
```

input() always returns a string. If you want a numeric type, then you need to convert the string to the appropriate type with the int(), float(), or complex() built-in functions.


## Output - string formatting 

In version 3.6, a new Python string formatting syntax was introduced, called the formatted string literal,  informally called f-strings.

The magic of f-strings is that you can embed Python expressions directly inside them. Any portion of an f-string that’s enclosed in curly braces ({}) is treated as an expression.

```
>>> s = 'bar'
>>> print(f'foo.{s}.baz')
foo.bar.baz
```
The interpreter treats the remainder of the f-string—anything not inside curly braces—just as it would an ordinary string. For example, escape sequences are processed as expected.

```
>>> s = 'bar'
>>> print(f'foo\n{s}\nbaz')
foo
bar
baz
```

You may prefix an f-string with 'r' or 'R' to indicate that it is a raw f-string. In that case, backslash sequences are left intact, just like with an ordinary string.

```
>>> z = 'bar'
>>> print(rf'foo\n{z}\nbaz')
foo\nbar\nbaz
```
Note: an f-string expression can’t be empty. An f-string expression can’t contain a backslash (\\) character.

## Command Line interfaces - argparse

The command line interface (also known as CLI) is a means to interact with a command line script. Python comes with several different libraries that allow you to write a command line interface for your scripts, but the standard way for creating a CLI in Python is currently the Python argparse library.

### When to Use a Command Line Interface

 The rule of thumb is that, if you want to provide a user-friendly approach to configuring your program, then you should consider a command line interface. Or if you’re used to setting variable values at the beginning of your scripts or manually parsing the sys.argv system list instead of using a more robust CLI development tool, 

Argparse had both positional and optional arguments that can be used to chnage the behavior of the program. 

For a tutorial look [here](https://docs.python.org/3/howto/argparse.html) and [here](https://realpython.com/command-line-interfaces-python-argparse/#what-is-a-command-line-interface). 

Some other alternatives to argparse are  click, docopt and invoke. 
[here](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/) for details and comparison between them. 
