# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:05:28 2023

@author: tshabe


1.Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computepay(hours, rate)

print("Pay:", pay)
