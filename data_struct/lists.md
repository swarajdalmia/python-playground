# Lists
Python lists are a collection of items in a particular order. The items don't have to be related or of a similar type either. Lists in python are denoted by "[]" and the items are seperated by ",". The items can be accessed by their index arr[i]. List are mutable and dynamic. Items from it can be removed and the list can be extended.  Even on appending items to a list, the id() paramerter which represents the reference remains unchanged.

- Lists are ordered.
- Lists can contain any arbitrary objects.
- List elements can be accessed by index.
- Lists can be nested to arbitrary depth.
- Lists are mutable.
- Lists are dynamic.

The low level complexity of operations on Lists, Sets and Dictionaries can be found {here}[https://www.ics.uci.edu/~brgallar/week8\_2.html].

len(arr) - returns the length of list object. 
List indeing starts with index 0 and is circular(to a certain extent), so -1 points to last element, but index len will give error out of bounds.  

## Changing/Adding/Removing Elements
- Modifying an item : arr[i] = newItem
- Appending an item(end) : arr.append(newItem)
    - Appending a list is a common way of dynamically building up a list.
- Insert elements at pos : arr.insert(pos, newItem) has 0(m) complexity.
- Removing an item with pos/index using del: del arr[pos]
- Removing an item with pop() : ele = arr.pop[i]
    - If we use pop(), we don't lose the element that we intent to remove.
    - using only .pop() treats the list as a stack and removes the last element
- Removing an item with name.  arr.remove(name) method deletes only the first occurrence of the object specified.

## Organising a List
- Permanent ordering : arr.sort() : changes ordering to alphabetic. The function arr.sort(reverse=True) sorts an array in reverse. However won't work if case isn't uniform.
- Temporary ordering : sorted(arr) : returns a temporary sorted version of a list. It accepts a reverse argument too
- Reverse the original order : arr.reverse()


## Slicing
- a[m:n] returns the portion of a from index m to, but not including, index n
- a[:4] + a[4:] == a will return True 
-  a[0:6:2] : strides(+ve/-ve) can be specified 
- a[::-1] : reverse an array 


## Python Operators 
- ele in list | ele not in list : check if element is present/not present in the list 
- + - concatenation, \* - replication
- len(), min(), and max() functions : min() works alphabetically as well 

## Creating Lists 
```
N = 5
arr = [0]*N 
rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
```

# Python Tuples
Tuples are identical to lists in all respects, except for the following properties:
type(var) : to check the type

- Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
- Tuples are immutable.
- Even though tuples are defined using parentheses, you still index and slice tuples using square brackets, just as for strings and lists.

## Why use a tuple as compared to a list ?

- Program execution is faster when manipulating a tuple than it is for the equivalent list.
- When you don’t want data to be modified.


For tuple, packing and unpacking look [here]{https://realpython.com/python-lists-tuples/}.
In Python, variable swap can be done with a single tuple assignment:
```
a, b = b, a
```









