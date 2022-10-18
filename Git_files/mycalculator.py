# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 06:09:17 2020

@author: Christian
"""

from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('460x400')

#Variables
global math
global calc_numbers
global result 

calc_numbers=[]
result = None
math = ''


#Functions
def my_click(number):
    global calc_numbers
    global result
    
    if type(result) != NoneType:
        result = None
        e.delete(0, END)
        e.insert(0, str(number))
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        
def addition():
    global calc_numbers
    global result
    global math
    
    if math == 'equal':
        current = e.get()
        calc_numbers = [current]
        e.delete(0, END)
        math = 'addition'
        return 
    if not calc_numbers:
        current1 = e.get()
        calc_numbers = [current1]
        e.delete(0, END)
        math = 'addition'
        return 
    if len(calc_numbers) == 1:
        current = e.get()
        e.delete(0, END)
        math = 'addition'
        result = int(calc_numbers[0]) + int(current)
        calc_numbers = [result]
        e.insert(0, str(result))
        return
    
def substraction():
    global calc_numbers
    global result
    global math
    
    if math == 'equal':
        current = e.get()
        calc_numbers = [current]
        e.delete(0, END)
        math = 'substraction'
        return 
    if not calc_numbers:
        current1 = e.get()
        calc_numbers = [current1]
        e.delete(0, END)
        math = 'substraction'
        return 
    if len(calc_numbers) == 1:
        current = e.get()
        e.delete(0, END)
        math = 'substraction'
        result = int(calc_numbers[0]) - int(current)
        calc_numbers = [result]
        e.insert(0, str(result))
        return
    
def multiplication():
    global calc_numbers
    global result
    global math
    
    if math == 'equal':
        current = e.get()
        calc_numbers = [current]
        e.delete(0, END)
        math = 'multiplication'
        return 
    if not calc_numbers:
        current1 = e.get()
        calc_numbers = [current1]
        e.delete(0, END)
        math = 'multiplication'
        return 
    if len(calc_numbers) == 1:
        current = e.get()
        e.delete(0, END)
        math = 'multiplication'
        result = int(calc_numbers[0]) * int(current)
        calc_numbers = [result]
        e.insert(0, str(result))
        return
    
def division():
    global calc_numbers
    global result
    global math
    
    if math == 'equal':
        current = e.get()
        calc_numbers = [current]
        e.delete(0, END)
        math = 'division'
        return 
    if not calc_numbers:
        current1 = e.get()
        calc_numbers = [current1]
        e.delete(0, END)
        math = 'division'
        return 
    if len(calc_numbers) == 1:
        current = e.get()
        e.delete(0, END)
        math = 'division'
        result = float(calc_numbers[0]) / float(current)
        calc_numbers = [result]
        e.insert(0, str(result))
        return

def equal():
    global clac_numbers 
    global result
    global math
    
    if math == 'equal':
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current))
    
    if math == 'addition':
        result = int(calc_numbers[0]) + int(e.get())
        #print result
        #print str(calc_number[0])
        e.delete(0, END)
        e.insert(0, str(result))
        math = 'equal'
        
    if math == 'substraction':
        result = int(calc_numbers[0]) - int(e.get())
        #print result
        #print str(calc_number[0])
        e.delete(0, END)
        e.insert(0, str(result))
        math = 'equal'
        
    if math == 'multiplication':
        result = int(calc_numbers[0]) * int(e.get())
        #print result
        #print str(calc_number[0])
        e.delete(0, END)
        e.insert(0, str(result))
        math = 'equal'
        
    if math == 'division':
        result = float(calc_numbers[0]) / float(e.get())
        #print result
        #print str(calc_number[0])
        e.delete(0, END)
        e.insert(0, str(result))
        math = 'equal'

#Test Harness
        
#def my_click(number):
#    current = e.get()
#    e.delete(0, END)
#    e.insert(0, str(current) + str(number))

#Number entry
e = Entry(root, width= 55, borderwidth= 5)
e.grid(row= 0, column= 0, columnspan = 4, padx= 10, pady= 20)

#Create buttons
num_0 = Button(root, text='0', padx= 33, pady= 20, command= lambda: my_click(0))
num_1 = Button(root, text='1', padx= 33, pady= 20, command= lambda: my_click(1))
num_2 = Button(root, text='2', padx= 33, pady= 20, command= lambda: my_click(2))
num_3 = Button(root, text='3', padx= 33, pady= 20, command= lambda: my_click(3))
num_4 = Button(root, text='4', padx= 33, pady= 20, command= lambda: my_click(4))
num_5 = Button(root, text='5', padx= 33, pady= 20, command= lambda: my_click(5))
num_6 = Button(root, text='6', padx= 33, pady= 20, command= lambda: my_click(6))
num_7 = Button(root, text='7', padx= 33, pady= 20, command= lambda: my_click(7))
num_8 = Button(root, text='8', padx= 33, pady= 20, command= lambda: my_click(8))
num_9 = Button(root, text='9', padx= 33, pady= 20, command= lambda: my_click(9))

add_button = Button(root, text= '+', padx= 33, pady= 20, command= addition)
sub_button = Button(root, text= '-', padx= 33, pady= 20, command= substraction)
mult_button = Button(root, text= 'x', padx= 33, pady= 20, command= multiplication)
div_button = Button(root, text= '/', padx= 33, pady= 20, command= division)

equal_button = Button(root, text= '=', padx= 33, pady= 20, command = equal)
clear_button = Button(root, text= 'Clear', padx= 110, pady= 20, command = equal)

#Display buttons
num_0.grid(row= 4, column= 1)
num_1.grid(row= 3, column= 0)
num_2.grid(row= 3, column= 1)
num_3.grid(row= 3, column= 2)
num_4.grid(row= 2, column= 0)
num_5.grid(row= 2, column= 1)
num_6.grid(row= 2, column= 2)
num_7.grid(row= 1, column= 0)
num_8.grid(row= 1, column= 1)
num_9.grid(row= 1, column= 2)

add_button.grid(row= 4, column= 3)
sub_button.grid(row= 3, column= 3)
mult_button.grid(row= 2, column= 3)
div_button.grid(row= 1, column= 3)

equal_button.grid(row= 5, column= 3)
clear_button.grid(row= 5, column= 0, columnspan=3)

root.mainloop()
