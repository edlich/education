# Coding Basics

## Author
This document was created by GitHub Copilot, an AI programming assistant.

## Table of Contents
1. [Introduction](#introduction)
2. [Variables and Data Types](#variables-and-data-types)
3. [Control Structures](#control-structures)
4. [Functions](#functions)
5. [Object-Oriented Programming](#object-oriented-programming)
6. [Resources for Further Learning](#resources-for-further-learning)

## Introduction
Coding, also known as programming, is the process of creating instructions for computers using programming languages. It's like writing a recipe that the computer follows to perform a specific task.

## Variables and Data Types
In programming, a variable is a storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value. The variable name is the usual way to reference the stored value.

Different data types include:
- Integer: Whole numbers (e.g., 1, 10, 200)
- Float: Decimal numbers (e.g., 1.1, 10.2, 200.5)
- String: Text (e.g., "Hello, World!")
- Boolean: True or False values

```python
# Integer
x = 10
print(x)

# Float
y = 20.5
print(y)

# String
z = "Hello, World!"
print(z)

# Boolean
a = True
print(a)
```

## Control Structures
Control structures determine the flow of a program. They include:

- If-Else Statements: Perform different actions based on different conditions.
- For Loops: Repeat a block of code a certain number of times.
- While Loops: Repeat a block of code while a certain condition is true.

```python
# If-Else Statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# For Loop
for i in range(5):
    print(i)

# While Loop
i = 0
while i < 5:
    print(i)
    i += 1
```

## Functions
A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

```python
def greet(name):
    print("Hello, " + name)

greet("World")
```

## Object-Oriented Programming
Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p = Person("John", 30)
p.greet()
```

## Resources for Further Learning
- [freeCodeCamp](https://www.freecodecamp.org/)
- [futureskills SH](https://futureskills-sh.de/kurse)
