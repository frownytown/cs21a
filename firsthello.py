#------------------------------------------------------------------------------------------
# Name:             firsthello.py
# Purpose:          The first python program
# Author:           Roger McClain
#-------------------------------------------------------------------------------------------
'''
A little python program that will print a greeting

Prompts the user for their name.
Prints a customized greeting essage.
'''
name = input('Please enter your name: ')    #prompt the user for their name
if name:
    print('Hello', str(name))   # print a personalized greeting
else:
    print('Hello Friend')
