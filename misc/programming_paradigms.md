# Programming Paradigms in Python

We will discuss the four paradigms mentioned below: 
- Functional 
- Imperative 
    - Procedural 
    - Object Oriented 

Python is a multi-paradigm programming language, once can choose the paradigm that best suits the problem at hand, mix different paradigms in one program, and/or switch from one paradigm to another as the program evolves.

## Functional Programming 

It is classified as a declarative language which uses expressions or declarations rather than statements as in imperative languages. It mimics the mathematical functions and avoids using changing states and mutable data. Since everything is immutable, it has no side effect (assuming that only the pure functional style is used, however python isn't purely functional; use haskell for a purely functional language). It follows the "what-to-solve" approach—that is, it expresses logic without describing its control flow.

The main advantage of this approach is that it lends itself well to parallel processing because there is no state to consider. Many developers prefer this coding style for recursion and for lambda calculus. 

Use of lambda expressions, map and functool are common.

Example: Sum of elements in a list, and squaring individual items in a list
```
import functools
my_list = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, my_list)
print(sum)

square = lambda x: x**2
print(list(map(square, my_list)))
``` 

## Imperative Programing 

Here, computation is performed as a direct change to program state. This style is especially useful when manipulating data structures and produces elegant yet simple code. Python fully implements this paradigm.

It executes commands in a step-by-step manner, just like a series of verbal commands. Following the "how-to-solve" approach, it makes direct changes to the state of the program; hence it is also called the stateful programming model. 


Example: Sum of elements in a list.
```
sum = 0
for x in my_list:
    sum += x
print(sum)
```

## Procedural Programming

It is a type of imperative programming, The tasks are treated as step-by-step iterations where common tasks are placed in functions that are called as needed. This coding style favors iteration, sequencing, selection, and modularization. 

In Python, each file behaves as a container (called as a module in Python) thus you can easily organize related items without difficulty. 

Example: Sum of elements in a list.
```
def do_add(any_list):
    sum = 0
    for x in any_list:
        sum += x
    return sum
print(do_add(my_list))
``` 

## Object Oriented Programming


This paradigm considers basic entities as objects whose instance can contain both data and the corresponding methods to modify that data. 

The concept of encapsulation allows an instance (object) to contain all related data and behaviors (methods). By encapsulation, the OOP style allows related data and methods to stick together. The concept of an inheritance provides reusability of data and methods, thus programmer needs to define only once for all the common data/methods in order to support multiple classes (a frame to create objects). The main disadvantage of the object oriented paradigm is that a program can easily become a complex monster and it can be difficult to classify everything.

Example: Sum of elements in a list.
```
class ListEvaluator:
	def __init__(self, lst):
		self.holding_list = lst
	def sum_list(self):
		result = 0
		for value in self.holding_list:
			result += value
		self.list_sum = result

evaluator = ListEvaluator([1, 2, 3, 4])
evaluator.sum_list()
print(evaluator.list_sum)
```
 







