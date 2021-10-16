from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from main import callAgain
import time

window = tk.Tk()
label = tk.Label(text="Your Texts:")
textFromMain = callAgain()
labelTwo = tk.Label(text = textFromMain)
textBox = tk.Label(text = " ")
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

widgetLabel = tk.Label(text="WPM,enter to start")
entry = tk.Entry()

label.pack()
labelTwo.pack()
widgetLabel.pack()
entry.pack()
textBox.pack()



def telempromter():
    words = len(textFromMain)
    wpm = int(entry.get())
    #list = textFromMain.split()
    for i in range (words):
        list = textFromMain.split()[i]
        textBox = tk.Label(text = list)
        textBox.pack()
        print(list)
        window.update()
    
        time.sleep(1/wpm)

def startProgram(event):
    for i in range (3):
        textBox = tk.Label(text = i+1)
        textBox.pack()
        window.update()
        time.sleep(1)
    
    telempromter()


window.bind("<Return>", startProgram)
window.mainloop()


