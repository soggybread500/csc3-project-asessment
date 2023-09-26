import tkinter as tk
from tkinter import *
from tkinter import StringVar


#command for quit
def quit():
    root.destroy()

#GUI
root = tk.Tk()
root.title('Countries and Capitals Quiz')
root.geometry('1000x1000')

#all questions
questions = ["What is the capital of New Zealand?",
             "What is the capital of Germany?",
             "Which country is Tokyo located in?",
             "Austria is located in which continent?",
             "What is the capital of India?",
             "What is the capital of South Korea ?",
             "What is the capital of Australia ?",
             "What is the capital of Canada?",
             "What is the capital of Italy ?",
             "What is the capital of Indonesia?"]
#all answer options
options = [['Auckland','Wellington','Christchurch','NZ doesnt exist','Wellington'],
           ['Berlin','Hamburg','Frankfurt','Munich','Berlin'],
           ['China','South Korea','U.S.A','Japan','Japan'],
           ['Europe','Oceania','North America','Asia','Europe'],
           ['New Delhi','Mumbai','Bengaluru','Surat','New Delhi'],
           ['Busan','Incheon','Seoul','Daegu','Seoul'],
           ['Perth','Canberra','Melbourne','Sydney','Canberra'],
           ['Vancouver','Ottawa','Toronto','Montreal','Ottawa'],
           ['Rome','Bologna','Venice','Florence','Rome'],
           ['Medan','Surabaya','Makasser','Jakarta','Jakarta']]

#images
backgroundimg = PhotoImage(file='/Users/Andy/Downloads/pink.png')

img1 = PhotoImage(file='/Users/Andy/Downloads/globe-1348777_1280.png')
img1 = img1.subsample(5) #resizing img1

#frame is the main window
frame = tk.Frame(root, bg='white', padx=10, pady=10)

#making the images labels and placing them
background=Label(frame, image=backgroundimg) #making the image a label
background.place(x=-15,y=-15) #placing the image as the background

questionimg=Label(root, image=img1, bg='#FCD5CE') #making the image a label
questionimg.place(x=365,y=120) #placing the image on the frame


#the pink square box
question_label = tk.Label(frame,height=25, width=35,bg='#FCD5CE',fg="black", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

#option 1 - 4 are the buttons for the answers
option1=Button(root, height=1, width=25, font=('Arial',25))
option2=Button(root, height=1, width=25, font=('Arial',25))
option3=Button(root, height=1, width=25, font=('Arial',25))
option4=Button(root, height=1, width=25, font=('Arial',25))

    
#next button
button_next = tk.Button(frame, text='Next', height=1, width=25, bg='Orange', font=('Verdana', 20))
                                           

#quit button
quitbutton=Button(root, text='Quit', font=('Verdana',20), command=quit)
quitbutton.place(x=270,y=100)
#quitbutton2=Button(root, text='Quit', font=('Verdana',20),height=1, width=25,
                   #command=quit)


frame.pack(fill="both", expand="true")
question_label.place(x=250, y=80)

option1.place(x=300,y=440)
option2.place(x=300,y=490)
option3.place(x=300,y=540)
option4.place(x=300,y=590)

button_next.place(x=300,y=640)


root.mainloop()

