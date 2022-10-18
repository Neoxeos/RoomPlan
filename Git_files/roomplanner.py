# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 00:20:43 2020

@author: Christian
"""

from tkinter import *
from tkinter import colorchooser

global WINDOW_WIDTH
global WINDOW_HEIGHT
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.geometry(str(WINDOW_WIDTH)+ 'x' + str(WINDOW_HEIGHT))
        self.master.title('room builder')
        self.bind("<Configure>", self.on_resize)
        self.pack(expand=True, fill='both')
        
#        other options to resize canvas
#        self.columnconfigure(1, weight=1)
#        self.rowconfigure(1, weight=1)
#        self.height = self.winfo_reqheight()
#        self.width = self.winfo_reqwidth()  
        
        #variables
        global CANVAS_WIDTH 
        global CANVAS_HEIGHT
        CANVAS_WIDTH = WINDOW_WIDTH/2
        CANVAS_HEIGHT = WINDOW_HEIGHT
        
        #left frame
        self.left_frame = Frame(self, bg='white smoke')
        self.left_frame.grid(row=0, column=0)
        
        #canvas
        self.canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,bg='bisque') #maybe highligththickness = 0 might fix window reshape
        self.canvas.grid(row=0, column=1,rowspan=3)
        self.canvas_color_button = Button(self.left_frame, text='click to set canvas color',command= self.changeCanvasColor)
        self.canvas_color_button.grid(row=5, column=0)
        
        #furniture length section
        self.label_furniture_length = Label(self.left_frame, text="Please enter length of furniture:",bg='white smoke')
        self.label_furniture_length.grid(row=1,column=0)
        self.furniture_length = Entry(self.left_frame,width=20, borderwidth=5)
        self.furniture_length.insert(0,'83') #default values
        self.furniture_length.grid(row=2,column=0,sticky=W)
        
        #furniture width section
        self.label_furniture_width = Label(self.left_frame, text="Please enter width of furniture:",bg='white smoke')
        self.label_furniture_width.grid(row=1,column=1)
        self.furniture_width = Entry(self.left_frame,width=20, borderwidth=5)
        self.furniture_width.insert(0,'50')
        self.furniture_width.grid(row=2, column=1,sticky=W)
        
        #list of canvas elements
        self.list_frame = Frame(self.left_frame, bg='orange')
        self.list_frame.grid(row=7, column=0)
        self.list_label = Label(self.list_frame, text='This is a list of all furniture in the room:')
        self.list_label.grid(row=0, column=0)
        
        #creating furniture section
        
        self.furniture_list = []
#        self.clicked = StringVar()
#        self.clicked.set('o')
#        
#        self.drop = OptionMenu(self.left_frame, self.clicked)
#        self.drop.grid(row=4, column=0)
        
        self.button_create_furniture = Button(self.left_frame, text='Click here to create a furniture item', command= lambda: self.createFurniture(self.canvas,self.convert()[0],self.convert()[1],self.convert()[2],self.convert()[3], 'blue'))
        self.button_create_furniture.grid(row=3, column=0,columnspan=4)
        self.button_furniture_color = Button(self.left_frame, text='Click here to choose a color for furniture', command= self.changeFurnitureColor)
        self.button_furniture_color.grid(row=6, column=0)
        
        
    def createFurniture(self,canvas,x_0,y_0,x_1,y_1,color):
        furniture = canvas.create_rectangle(x_0,y_0,x_1,y_1,fill=color)
        self.furniture_list.append(furniture)
        
    
    def changeFurnitureColor(self):
        color = colorchooser.askcolor()[1] #getting the hex code here
    
    def changeCanvasColor(self):
        color = colorchooser.askcolor()[1] #getting the hex code here
        self.canvas.config(bg = color)
    
    def clearALL(self):
        pass
    
    def rescale(self):
        pass
    
    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        global CANVAS_WIDTH
        global CANVAS_HEIGHT
        wscale = float(event.width)/CANVAS_WIDTH
        hscale = float(event.height)/CANVAS_HEIGHT
        CANVAS_WIDTH = event.width
        CANVAS_HEIGHT = event.height
        # resize the canvas 
        self.canvas.config(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
#       rescale all the objects tagged with the "all" tag
        self.canvas.scale("all",0,0,wscale,hscale)
        
    def convert(self):
        '''
           length is horizontal,
           width vertical
        '''
        #((Lc-Lf)/2, (Wc-Wf)/2, (Lc+Lf/2), (Wc+Wf)/2) => formula
        length_furniture = float(self.furniture_length.get())
        width_furniture = float(self.furniture_width.get())
        
        x_0 = (float(CANVAS_WIDTH)-length_furniture)/2
        y_0 = (float(CANVAS_HEIGHT)-width_furniture)/2
        x_1 = (float(CANVAS_WIDTH)+length_furniture)/2
        y_1 = (float(CANVAS_HEIGHT)+width_furniture)/2
        return [x_0,y_0,x_1,y_1]

class Bed(App):
    def __init__(self):
        pass
    
    def create(self):
        pass
        
def main():
    if __name__ == '__main__':
        root = Tk()
        my_app = App(root) 
        my_app.mainloop()
main()
        
