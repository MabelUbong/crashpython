# -*- coding: utf-8 -*-
"""session_two_exercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/warwickdatascience/beginners-python/blob/master/session_two/session_two_exercises.ipynb

<a href="https://colab.research.google.com/github/warwickdatascience/beginners-python/blob/master/session_two/session_two_exercises.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

<center>Spotted a mistake? Report it <a href="https://github.com/warwickdatascience/beginners-python/issues/new">here</a></center>

# Beginner's Python—Session Two Homework Exercises

## User Input

Ask the user for the year, month, and day and use these to print out the date in the following format:

`Your date is 1 January, 1970`

(Hint: if you want to get the comma looking exactly right, you might have to use string addition)
"""

year = input("What year is it? ")
month = input("What month is it?")
day = input("What day of the month is it?")

print("Your date is", day, month +",",year)

"""Ask the user to input a decimal number (remember you'll need to use `float()` to convert it from a string). Multiply this $5$, subtract $1.2$ and print the result"""

num= float ( input("Write a decimal number "))
print( "The number is", num*5 -1.2)

"""## Variable Types

What happens when you pass a decimal number (such as $3.14$) to `int()`?
"""

int(3.14)

"""The number is rounded

The `min()` and `max()` functions are versatile. As well being able to input a list of numbers, you are able to pass multiple inputs to these functions, separated by commas, provided they are all of the same type. For example:
"""

min(2, 5, 1)

"""The versitility doesn't stop there. What happens if we put in two strings as the inputs to either `min()` or `max()`. Experiment and try to find out.

(Hint: Try comparing each pair of `Cat`, `Dog`, and `Donkey`)
"""

print(max("Dogs", "Donkey"))
print( max("Cat", "Dogs", "Donkey"))

"""Orders alphabetically

Say you wanted to add the string `"Time is 12:"` to the integer `30` to get the string `"Time is 12:30"`. How can you use type conversion to achieve this?
"""

min = 30
rou = str(min)
print("Time is 12:" + rou)

"""## Sum, Min, Max and Length

Your teammates are aged 20, 33, 45, 57, and 62. Use `input()` to get Python to ask you your age and then make a list containing the 5 ages above and your age
"""

teammates = [20,33,45,57,62]
age = int ( input("How old are you? "))
all_ages = [20,33,45,57,62,age]
print(all_ages)

"""Find the average age of your team and print it

(Hint: The average age is the `sum` of all ages divided by the `len`gth of your list of ages)
"""

total = sum(all_ages)
num = len(all_ages)
average = print("Average team ages is", total/num)

"""Run the following lines of code to create two lists containing the scores of 30 students in each class"""

from random import randrange, seed
seed(1729)
class_A_scores = [randrange(101) for __ in range(30)]
class_B_scores = [randrange(101) for __ in range(30)]

"""Use `max()` to find which class contained the highest scoring student"""

print("The best scoring students in class A and B were", max(class_A_scores), "&", max(class_B_scores), "respectively")

"""As mentioned above, you can find the minimum or maximum of a collection of numbers without having to first put them in a list. Use this approach to find the minumum and maximum of the numbers 4, 5, 2, and 8"""

print("Max:",max(4, 5, 2, 8))
print("Min:",min(4, 5, 2, 8))

print("High:", max(4,5,2,8))
print("Low:", min(4,5,8,2))

"""Ask the user for two strings and print the length of the shortest"""

string_1 = input("Write something? ")
string_2 = input("Write something else? ")
print("The shortest string has",
      min(len(string_1), len(string_2)),
          "characters")

