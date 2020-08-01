# Python Project Setup 

## Structure of a python project 

[Open sourcing a python project the right way](https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/).

- talks about directory structure, inclusive of some of the important files. 
- discusses the setuptools and setup.py 
- discussed the use of github, for version control, open sourcing, talks about how to use the issues page to to keep all of the information related to bug fixes, enhancements, and feature requests.
- tox can be used to test across various verisons of python

## sphinx

It's used to generate the Python's official documentation and the documentation for almost all other popular Python packages. It was written with idea of making auto-generation of HTML documentation from Python code as easy as possible.

## Continuous Integration with TravisCI

Continuous Integration refers to the process of continuously integrating all changes for a project (rather than periodic bulk updates). For our purposes, it means that each time we push a commit to GitHub our tests run, telling us if the commit broke something. As you can imagine, this is an incredibly valuable practice. There's no more "forgetting to run the tests" before committing/pushing. If you push a commit that breaks the tests, you'll get an email telling you so.


## PyPI 

The Python Package Index (formerly known as "the Cheeseshop") is a central database of publicly available Python packages. PyPI is where your project's releases "live." Once your package (and its associate meta-data) has been uploaded to PyPI, others can download and install it using pip or easy_install. 

## git Workflow With git-flow

use the very popular git-flow model of branching.
 
The develop is the branch you'll be doing most of your work off of; it's also the branch that represents the code to be deployed in the next release. feature branches represent non-trivial features and fixes that have not yet been deployed (a completed feature branch is merged back into develop). Updating master is done through the creation of a release.

git-flow needs to be installed. 

A blog explanation of [git-flow](https://jeffkreeftmeijer.com/git-flow/).


## setup
What is the use of setup.py ?
setup.py is usually used to create distribution formats (wheels) of python packages so you can upload them on PyPi for others to easily install via pip install <yourpackage>.

having an init() in a folder also creates a package however they are a different type. they are import packages, while the one with setup.py are distribution packages. 

They contain additional metadata for managing an installation as well, such as dependencies on other distribution packages, version identifiers for managing upgrades. [reddit](https://www.reddit.com/r/learnpython/comments/fq8uba/what_is_the_actual_use_of_setuppy/?sort=top). 

setup.py is Python's answer to a multi-platform installer and make file [stackoverflow](https://stackoverflow.com/questions/1471994/what-is-setup-py). 

[creating and distributing a package](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html)

## Linter

Linting is the automated checking of your source code for programmatic and stylistic errors. This is done by using a lint tool (otherwise known as linter). A lint tool is a basic static code analyzer.

Linting is important to reduce errors and improve the overall quality of your code. Using lint tools can help you accelerate development and reduce costs by finding errors earlier.

Lint was the name of a program that would go through your C code and identify problems before you compiled, linked, and ran it. 

Uses of linters:
- Flagging bugs in your code from syntax errors
- Giving you warnings when code may not be intuitive
- Providing suggestions for common best practices
- Keeping track of TODO’s and FIXME’s
- Keeping a consistent code style

- Python: Flake8 is the most popular python linter and black is the most opinionated and simple to use python linter. Black linter is really good and is really good for a basic python linting. The 2 features missing in black are import sorting and finding unused imports/vars. Isort solves the former and flake8-black solves for the latter.

Look at differences between linters and static type checkers.

## Static Type checkers

Mypy is the most common and widely used python static type checker. Though it’s a non-trivial amount of effort to make sure that your python code has proper types defined, it’s completely worth the effort. The tool provides many options to turn on and off various different kinds of checks. The one I really appreciate is the option to run the checker only on any new code, this makes it possible to add this to an existing repo and add types incrementally in your project.

## Testing 

Pytest is the most popular python testing framework with > 6000 github stars. Pytest provides a much simpler interface and lower boilerplate code. It’s fast, stable and feature rich.

In the Python automated testing ecosystem, there are two main alternatives to the (quite usable) Python standard library unittest package: nose and py.test.Both extend unittest to make it easier to work with while adding additional functionality. 


## Coverage 

 It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not.

Coverage is the most common python coverage tool with > 1000 github stars. It works nicely with pytest and has options to enforce the coverage threshold only on any newly written code in your project.

ref:
- [State-of-the-art python project setup](https://towardsdatascience.com/state-of-the-art-python-project-setup-82a046fc1f20)

