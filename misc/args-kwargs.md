# \*args and \*\*kwargs

\*args and \*\*kwargs allow you to pass multiple arguments or keyword arguments to a function.

```
def my_sum(a, b):
    return a + b
```

This function works fine, but it’s limited to only two arguments. What if you need to sum a varying number of arguments, where the specific number of arguments passed is only determined at runtime? Wouldn’t it be great to create a function that could sum all the integers passed to it, no matter how many there are?

One could do that by passing a list and well as a set. 

## \*args

This is where \*args can be really useful, because it allows you to pass a varying number of positional arguments. 

```
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```
(\*) is the unpacking operator. the iterable object you’ll get using the unpacking operator * is not a list but a tuple.

Note: args is just a name and one can instead use whatever name one wants. 

## \*\*kwargs

\*\*kwargs works just like \*args, but instead of accepting positional arguments it accepts keyword (or named) arguments. 

```
# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

the kwargs converts its input into a dict object. 

## Unpacking With the Asterisk Operators: \* & \*\*

The single asterisk operator \* can be used on any iterable that Python provides, while the double asterisk operator \*\* can only be used on dictionaries.

For more details look [here](https://realpython.com/python-kwargs-and-args/).

some interesting examples:
```
# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list
```

```
$ python extract_list_body.py
1
[2, 3, 4, 5]
6
```

merging two lists:
```
# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]
```

merging dicts:
```
# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
```



