# Strings 

### Diff. between '' and ""
In python there is no functional difference between '' and "". However is there is an apostophe ' in the string 
one should only use "" and if there is a mention of quotes within "" then '' should be used. String literals inside triple quotes, """ or ''', can span multiple lines of text. i

### Immutability 
Python strings are immutable i.e. they cant be edited after they are created. So string operations create new strings. This can be checked using the function id(). A string after lets say an operation like concat will reference a different id. 

### Compexity
Since strings are immutable. String concatenation requires all characters to be copied, this is a O(N+M) operation (where N and M are the sizes of the input strings). Instead concatenation of strings if done more than once should be done with "".join(l\_words) where l\_words stands for a list words. The time complexity is analysed in depth [here](https://waymoot.org/home/python_string/).

### String Formatting 
Python 3.6 introduced f-strings, a new way to format strings. Its concise, less prone to error and faster.
The earlier ways were %-formatting and str.format(). f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. For more details one can look [here](https://realpython.com/python-f-strings/#option-2-strformat).

### Efficent Memory 
Does defining a string twice (associated with 2 different variable names) create one or two objects in memory?
For example, writing animal = 'dog' and pet = 'dog'.
It only creates one. This is unintuitive but can be verified with id(). There must be limitations though. What are they ?

### Misc.
Taken from [here](https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8). 
- string idenity, ==(checks for equality) vs is(checks for idenity i.e. they both point to the same ref)
- id() function returns the id of a memory address associated with a name.
- to check is a substring exists in a string use "in".
- index of first occurance of substring. find() and index(). If not found find() returns -1 and index() returns ValueError.
- count('a') - counts the number of times the char 'a' occurs in the string
- capitalize() - capitalises the first character of a string 
- integers cannot be appended to string in python with "+".
- "c".join(list) : joins every character in the list with character c between the items.
- reversed(sequence) : returns an iterator that reverses the input sequence which can be a string or a list.
- str() : convert an interger to a string
- str.replace(str1, str2) : replaces all instances of str1 with str2 in the string str.
