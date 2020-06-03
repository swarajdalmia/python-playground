#Sets

- Sets are unordered.
- Set elements are unique. Duplicate elements are not allowed.
- A set itself may be modified, but the elements contained in the set must be of an immutable type, therefore tuples can be elements but lists/dictionaries can't be.
- The elements in a set can be objects of different types.
- Python provides another built-in type called a frozenset, which is in all respects exactly like a set, except that a frozenset is immutable.

## Creating a Set 
A set can be created with x = set(\<iterable\>).
Alternatively, one can use curly braces, x = {\<obj\>, \<obj\>, ..., \<obj\>}

```
s = 'quux'
var = set(s)
x = {'q', 'u', 'u', 'x'}
```

### Size and Membership 
len() for size and "in" to check membership.

## Set operations 
- Union : x1|x2 , x1.union(x2)
- Intersection : x1&x2 , x1.intersection(x2)
- Set difference : x1-x2 , x1.difference(x2)
- Symmetric Difference : x1 ^ x2 , x1.symmetric\_difference(x2)
- x1.isdisjoint(x2) : returns true or false based on if the sets are disjoint 
- x1.issubset(x2)
- x1 < x2 : proper subset 

## Modify a Set
- x.add(\<elem\>)
- x.remove(\<elem\>)










