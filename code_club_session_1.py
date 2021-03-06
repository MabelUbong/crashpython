# -*- coding: utf-8 -*-
"""Code Club Session 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/warwickdatascience/beginners-python/blob/master/session_one/session_one_blank_template.ipynb

<a href="https://colab.research.google.com/github/warwickdatascience/beginners-python/blob/master/session_one/session_one_blank_template.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

<center>Spotted a mistake? Report it <a href="https://github.com/warwickdatascience/beginners-python/issues/new">here</a></center>

# Beginner's Python—Session One Template

## Printing

### Introduction

Get Python to print "Hello World"
"""

print("hello world")

Print the number 5

print(5)

"""Print the product of 5 and 10"""

print(5*10)

"""Print both text and arithmetic"""

print("hello world", 5*10)

"""### Standard Puzzles

Print your name using the print command
"""

print("mabel")

"""Print your three favourite colours"""

print("purple","blue","green")

"""Calculate $26\times66+13$"""

print((26*66)+13)

"""Calculate $6804 \div 162$"""

print(6804/13)

"""### Bonus Puzzles

Calculate $2^8$
"""

print(2**8)

"""What happens if you put a mathematical expression in double quotes when you are printing?"""

# try it on the next line and then write your answer in the next cell
print((2**8))

"""Calculate $6804\div162$ using integer division"""

print((6804/162))

"""## Variables

### Introduction

Create two variables, storing your name and age
"""

name = "mabel"
age = 19

"""Create a variable containing your favourite food and print this as a sentence"""

favourite_food = "sushi"
print("my favourite food is", favourite_food)

"""### Standard Puzzles

Use the name and age variables from above to print a sentence
"""

print("my name is", name, "and i am", age)

"""### Bonus Puzzles

Print what your age will be in 5 year's time as a sentence
"""

print("i will be", age+5, "in 5 years time")

"""Create a variable with value $n$ the print $n$, $2n$, and $n-1$. Give the variable a new value and reprint these values. How did using variables make this easier?"""

# write your code in this cell and answer in the next cell

random = 2
print(random, 2*random, random-1 )

"""We can change the variable vaule easily

## Manipulating Variables

### Introduction

Overwrite the value of a variable
"""

x = 2
x = 3
print(x+x)

"""Create a new variable based on the value of another variable"""

y=x-1
print(y)

"""Overwrite a variable with a new value based on its current value"""

x=4
x=5
print(y-x)

"""### Standard Puzzles

What do you think the value of `y` will be in the presentation code?

Python remembers the last assigned value

## Variable Types

### Introduction

Create one variable for each of the types integer, float, and string. Check their types using the `type()` function
"""

x = 1
y = 1.2
z = "number"

print(type(x))
print(type(y))
print(type(z))

"""Create a string variable that contains the digits of a number. Create a new variable by converting this string to an integer. Print the types of both variables"""

string_digits = "1234"
interger_digits = int (string_digits)
print(type(string_digits))
print(type(interger_digits))

"""### Standard Puzzles

Define the variables `x`, `y`, and `z` as in the presentation. What are their types?
"""

x = 2
y =2.0
z ="2"
print(type(x))
print(type(y))
print(type(z))

"""Add two string variables together and print the result"""

# try it here and write your response below
value_1 = "2"
value_2 = "2"
print(value_1 + value_2)

"""No space between the values

### Bonus Puzzles

What happens if we omit don't wrap `type()` in `print()`?

It will print the last value out

Try multiplying a string by an integer. What happens?
"""

test  ="example"
print(test*4)

"""Multplying a string by integer concatenates repititions of the string"""