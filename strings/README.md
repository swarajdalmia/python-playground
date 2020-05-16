# Strings 

### Diff. between '' and ""
In python there is no functional difference between '' and "". However is there is an apostophe ' in the string 
one should only use "" and if there is a mention of quotes within "" then '' should be used. String literals inside triple quotes, """ or ''', can span multiple lines of text. i

### Immutability 
Python strings are immutable i.e. they cant be edited after they are created. So string operations create new strings. 

### Compexity
Since strings are immutable. String concatenation requires all characters to be copied, this is a O(N+M) operation (where N and M are the sizes of the input strings). Instead concatenation of strings if done more than once should be done with "".join(l\_words) where l\_words stands for a list words. The time complexity is analysed in depth [here](https://waymoot.org/home/python_string/).

### Interesting Questions
Taken from [here](https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8). 
- string idenity, ==(checks for equality) vs is(checks for idenity i.e. they both point to the same ref)
- id() function returns the id of a memory address associated with a name.
- to check is a substring exists in a string use "in".
- index of first occurance of substring. find() and index(). If not found find() returns -1 and index() returns ValueError.
- count('a') - counts the number of times the char 'a' occurs in the string
- capitalize() - capitalises the first character of a string 
- 
