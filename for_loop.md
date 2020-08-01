# Pythonic looping 

First specify a list,dictionary.
```
odd_num = [1,3,5,7,9]
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
```

- Simply iterate over list/dictionaries.

```
for i in odd_num:
    print(i)

for key in a_dict:
    print(key, '->', a_dict[key])
```

The above format can be used to loop over any iterable. For strings it iterates over characters, for dictionaries over keys, for a file over the file lines.  


- Use an index
```
for i in range(len(odd_num): 
    print(odd_num[i]) 
```

- Using enumerate. When one wants both index and value. 
```

for i, val in enumerate(odd_num): 
    print (i, ",",val)
```

## Without explicit loop structure 


### Use list comprehension
This makes the use of generators. What are generators ? They are a consise way of making new lists. 
Nested for/if can be specified linearly. If one used braces the format changes as seen in this {example}[https://stackoverflow.com/questions/3766711/advanced-nested-list-comprehension-syntax]. However, not all for loops can be written in this form. can one use else ?


```
[do_somethign_with(item) for item in odd_num if filter_condition(i)]  
```

If the outer braces are "[" then a list is returned, "(" a iterator is returned and it is called a generator expression. 

The walrus operator allows to run an expression while simultaneouly assigning output. 
```
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
```

### Using Map 
This is the functional programming approach, instead of using list comprehension. 

```
doubled_list = map(lambda x: x * 2, old_list)
```
The syntax for map is map(function, iterable). Above a function is specified using lamda x.

#### Lambda 

- A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.

```
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
```

### Using Reduce

If you want to reduce a sequence into a single value.

```
from functools import reduce
summation = reduce(lambda x, y: x + y, numbers)
```
First two elements of the list are picked and the result is obtained. Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.

