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

## Does Python use pass by value or pass by reference ?

Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”. In the event that you pass arguments like whole numbers, strings or tuples to a function, the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function. The only way to change an immutable obj is to reassign it, and when that is done, the object pointer within the scope of the function points to another id now. 

Whereas passing mutable objects can be considered as call by reference because when their values are changed inside the function, then it will also be reflected outside the function.

When say a string which is an immutable type of object is passed as argument to the function. Within the scope of the given function a "new value" has been bounded to the object. Within the scope of the function we modify “old value”` to “new value”. Once we leave the scope of function the "new value" is no longer in the name space, and the value that string refers to was never changed on the outside.

Look at the answer by Kirk Strauser [here](https://stackoverflow.com/questions/13299427/python-functions-call-by-reference?answertab=votes#tab-top).
