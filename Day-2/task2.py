# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:03:22 2023

@author: tshabe
"""

score = float(input("Enter score between 0.0 and 1.0: "))

if score < 0.0 or score > 1.0:
    print("Error: score out of range")
elif score >= 0.9:
    print("Grade: A")
elif score >= 0.8:
    print("Grade: B")
elif score >= 0.7:
    print("Grade: C")
elif score >= 0.6:
    print("Grade: D")
else:
    print("Grade: F")
