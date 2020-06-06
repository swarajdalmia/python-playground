# ZIP() 

Python’s zip() function creates an iterator that will aggregate elements from two or more iterables, where the i-th tuple contains the i-th element from each of the argument iterables. The iterator stops when the shortest input iterable is exhausted.

zip() is available in the built-in namespace. use dir(__builtins__).

zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets etc.

```
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> zipped = zip(numbers, letters)
>>> zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
>>> list(zipped) 
[(1, 'a'), (2, 'b'), (3, 'c')]
```

Normally the order is kept intact, except in the case of the set iterable. 

### next()

list(zipped) can only be called once, on the second time, it shows a StopIteration exception. 
- next(zipped) returns the first tuple. If list(zipped) is called after calling next() once, then only the remaining elements 
are printed.

### Arguments of unequal length

- In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable. 
- If trailing or unmatched values are important to you, then you can use itertools.zip\_longest() instead of zip(). With this function, the missing values will be replaced with whatever you pass to the fillvalue argument (defaults to None). 


### Python 2 vs 3

In python 2, zip() returned a list of tuples; in python 3, an iterator is returned. 
In Python 3, one can emulate the Python 2 behavior of zip() by wrapping the returned iterator in a call to list(). 
In python 2, to get an iterator, one needs to use itertools.izip()

## Loops 

Traversing lists and dictionaries in parallel. 

```
for l, n in zip(letters, numbers):
# traversing dictionaries in parallel
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
```

## Unzipping a sequence 

If one has a list of tuples and wants to separate the elements of each tuple into independent sequences, then one can use zip() along with the unpacking operator \*.

```
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3, 4)
>>> letters
('a', 'b', 'c', 'd')
```

## Building Dictionaries 

```
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
```

One can also update dictionaries using ```a_dict.update(zip(field, new_job))```.



