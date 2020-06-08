# Shallow and Deep Copy

What is the difference between shallow copy, deep copy and normal assignment ?

```
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
```

Using normal assignment:
- Normal assignment just creates another name that points to the exact same place as the earlier one 

```
d = c

print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
```

Using a shallow copy:
- Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the original.

```
d = copy.copy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
```

Using a deep copy:
- it recursively creates a seperate copy of all the nested objects. The clone is fully independent of the original, but creating a deep copy is slower.

```
d = copy.deepcopy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object
```


- However, if you just want to copy a simple list, deep copy and shallow copy don't differ in functionality. 


