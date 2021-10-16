from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from main import callAgain

window = tk.Tk()
label = tk.Label(text="Your Texts:")
labelTwo = tk.Label(text = callAgain())

widgetLabel = tk.Label(text="WPM")
entry = tk.Entry()

label.pack()
labelTwo.pack()
widgetLabel.pack()
entry.pack()

window.mainloop()
