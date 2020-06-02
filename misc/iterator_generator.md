# Iterators 

Iterator is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic. 

- Iterators are objects that contain countable values(but not finite).
- An interator is an object that can be iterated upon.
- Iterators must implement the iterator protocols, namely the methods \_\_iter\_\_() and  \_\_next\_\_()

Iterators have several advantages:

- Cleaner code
- Iterators can work with infinite sequences
- Iterators save resources
    - when working with iterators, we can get the next element in a sequence without keeping the entire dataset in memory(example reading files with open).

## Iterators vs Iterable

Lists, tuples, dictionaries, sets, strings are all iterable objects. They are iterable containers which you can get an iterator from.
- iter() method takes an iterable and returns an iterator. Iterable objects call the method __iter__() in them.
 
```
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

# If there are no more elements on using next() a StopIteration Exception is raised. The StopIteration exception will cease the for loop and in user defined iterators within [next]{http://zetcode.com/lang/python/itergener/}.

print(next(myit))
print(next(myit))
print(next(myit))

```

- To create a User Defined iterator. Look at example [here]{https://www.w3schools.com/python/python\_iterators.asp]


# Generators

Generators simplifies creation of iterators and are special routines which return iterators. 

- Are defined with the def keyword just like functions
- Use the yield keyword
- May use several yield keywords 

[Example]{http://zetcode.com/lang/python/itergener/}.

The yield keyword exits the generator and returns a value. To reach the first and successive yield lines one has to use the next function. When there is nothing left to yield, a StopIteration exception is raised.

## Generator Expressions

Generator expression is similar to a list comprehension. The difference is that a generator expression returns a generator, not a list and used () instead of [] as outer most braces.

```
n = (e for e in range(50000000) if not e % 3)
```

Creating a list comprehension in this case would be very inefficient because the example would occupy a lot of memory unnecessarily. Insted of this, we create a generator expression, which generates values lazily on demand.

# Itertools 

The itertools module in the standard library provides lot of intersting tools to work with [iterators]{https://anandology.com/python-practice-book/iterators.html}.

- itertools.chain() : to chain multiple iterators, i.e. append one after the other.
- izip : iterable version of zip












