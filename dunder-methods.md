# Dunder Methods 

They are also called magic methods. Method names that have leading and trailing double underscores are reserved for special use like the '__init__' method for object constructors, or '__call__' method to make object callable. These methods are known as dunder methods. dunder here means “Double Under (Underscores)”. 

[Why wrap them in double underscrores ?](https://medium.com/python-features/magic-methods-demystified-3c9e93144bf7)

```
class LenDefined:
    def __len__():
        return 1
>>> obj = LenDefined()
>>> len(obj)
1
```

[Examples of predefined dunders](https://dbader.org/blog/python-dunder-methods)

