# Lists
Python lists are a collection of items in a particular order. The items don't have to be related or of a similar type either. Lists in python are denoted by "[]" and the items are seperated by ",". The items can be accessed by their index arr[i]. List are mutable and dynamic. Items from it can be removed and the list can be extended.  Even on appending items to a list, the id() paramerter which represents the reference remains unchanged.

- Modifying an item : arr[i] = newItem
- Appending an item(end) : arr.append(newItem)
    - Appending a list is a common way of dynamically building up a list.
- Insert elements at pos : arr.insert(pos, newItem)
- Removing an item from pos using del: del arr[pos]
- Removing an item with pop() : ele = arr.pop[i]
    - If we use pop(), we don't lose the element that we intent to remove.
    - using only .pop() treats the list as a stack and removed the last element
  

 
