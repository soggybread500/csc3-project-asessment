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
option1=Button(root, height=1, width=25, font=('Arial',25),
                         command = lambda : checkAnswer(option1))
option2=Button(root, height=1, width=25, font=('Arial',25),
                         command = lambda : checkAnswer(option2))
option3=Button(root, height=1, width=25, font=('Arial',25), 
                         command = lambda : checkAnswer(option3))
option4=Button(root, height=1, width=25, font=('Arial',25),
                         command = lambda : checkAnswer(option4))

    
#next button
button_next = tk.Button(frame, text='Next', height=1, width=25, bg='Orange', font=('Verdana', 20), 
                        command = lambda :[displayNextQuestion()])
                                           

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



# create a function to disable buttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

index = 0
correct = 0
count = 1

# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index, count
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    count += 1
    disableButtons('disable')

# question count (# out of 10)
questioncount=Label(frame, height=1, width=10, font=('Arial', 15),
                    bg='#FCD5CE', fg='black', wraplength=500)
questioncount.place(x=605,y=90)



# function to display the next question
def displayNextQuestion():
    global index, correct, count
    if button_next['text'] == 'Play Again':
        correct = 0
        index = 0
        count = 1
        question_label['bg'] = '#FCD5CE'
        questioncount['bg'] = '#FCD5CE'
        button_next['text'] = 'Next'
        questionimg['bg'] = '#FCD5CE'
        
        

    if index == len(options):
       question_label['text'] = str(correct) + " out of " + str(len(options))
       button_next['text'] = 'Play Again'
       
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
           questioncount['bg'] = 'green'
           questionimg['bg'] = 'green'
       else:
            question_label['bg'] = 'red'
            questioncount['bg'] = 'red'
            questionimg['bg'] = 'red'



    else:
        question_label['text'] = questions[index]
        questioncount['text'] = str(count) + " out of " + str(len(options))
    
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Finish'


displayNextQuestion()

root.mainloop()

