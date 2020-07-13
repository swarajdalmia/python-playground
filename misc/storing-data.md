# Storing data

The json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs. You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn.

JSON (JavaScript Object Notation) format was originally developed for JavaScript.

- saving information 
```
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj: 
    w json.dump(numbers, f_obj)
```

- loading back information 
```
import json
filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

