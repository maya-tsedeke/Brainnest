# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:14:47 2023
Write a program which repeatedly reads numbers until the
user enters `done`. Once `done` is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

functions to be used:

sum() - len() - sum()/len()
or
from statistics import mean
mean()

@author: tshabe
https://github.com/maya-tsedeke/Brainnest
"""

numbers = []
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        num = float(number)
        numbers.append(num)
    except:
        print("Invalid input")

if len(numbers) == 0:
    print("No numbers entered")
else:
    total = sum(numbers)
    count = len(numbers)
    average = total/count
    print(total, count, average)
