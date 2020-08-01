# Working with files

## Reading from a file 

The file one wants to read from is 'pi\_digits.txt'. 
The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents the close() statement from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call close() too early in your program, you’ll find yourself trying to work with a closed file (a file you can’t access), which leads to more errors. It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the time is right. 

```
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

There is an extra blank line printed at the end becasue read() returns an empty string when it reached EOF. Use rstrip() along with print to remove the extra line. 

Note : When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.

## Reading Line by line 

```
with open(filename) as file_object: 
    for line in file_object:
        print(line)
```

When we print each line, we find even more blank lines. print() adds a blank line of its own and each line itself has a newline character at the end. 

- Making a List of Lines from a File 
```
with open(filename) as file_object:
    lines = file_object.readlines()
```
## Working with large files

Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.

## Writing to an empty file

```
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.

The open() function automatically creates the file you’re writing to if it doesn’t already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the file before returning the file object.

Note: Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

