# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:41:10 2023

@author: tshabe

Problem: Code line repeatition in the following code
# problem
print('Good morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')


solution 
1. use function and for loop
2. use function
3. use for loop without function

https://github.com/maya-tsedeke/Brainnest
"""

#1. use function and for loop
def ask_feeling(greeting):
    print(greeting)
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')

greetings = ['Good morning!', 'Good afternoon!', 'Good evening!']
for greeting in greetings:
    ask_feeling(greeting)
    
    #.2 Using Function without for loop
    """----------------------------------------------------------------------"""
    def ask_feeling(greeting):
        print(greeting)
        print('How are you feeling?')
        feeling = input()
        print('I am happy to hear that you are feeling ' + feeling + '.')

    ask_feeling('Good morning!')
    ask_feeling('Good afternoon!')
    ask_feeling('Good evening!')

#1. Using  for loop without
"""----------------------------------------------------------------------"""
greetings = ['Good morning!', 'Good afternoon!', 'Good evening!']
for greeting in greetings:
    print(greeting)
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')
    

