import tkinter as tk
from tkinter import filedialog
import time
import threading

lineStartX = 20
lineStartY = 90
lineEndX = 380
lineEndY = 93

x0 = lineStartX
y0 = lineStartY
x1 = lineEndX
y1 = lineEndY

speech = "So I first came to Chicago when I was in my early twenties, and I was still trying to figure out who I was; still searching for a purpose to my life. And it was a neighborhood not far from here where I began working with church groups in the shadows of closed steel mills."

speech = speech.split()

window = tk.Tk()

#set up so button is clicked it opens file
# file = filedialog.askopenfile(parent = window, mode='rb', title='Choose a file')
# if file:
#     data = file.read()
#     file.close()
#     print( "I got %d bytes from this file." % len(data))


window.title("Teleprompter")
window.geometry('400x400')

# canvas = tk.Canvas(window)
# canvas.configure(bg="white")
# canvas.pack(fill="both", expand=True)


stop = True
currentIndex = 0
currentState = 0
interval = 0.6



# currentLabel = tk.Label(canvas, text="So I first came to Chicago when I was in my", font=("Arial", 18))
# nextLabel = tk.Label(canvas, text="early twenties, and I was still trying to", font=("Arial", 18))
# currentLabel.place(x=lineStartX + 5, y=lineStartY-29)
# nextLabel.place(x=lineStartX + 5, y=lineStartY+50)

# line = canvas.create_rectangle(x0, y0, x1, y1, fill='green')
wordLabel = tk.Label(window, text="dfvx", font=("Arial", 27))
wordLabel.place(x=200, y=200, anchor='center')

wpmLabel = tk.Label(window, text="WPM: ", font=("Arial", 18))
wpmLabel.place(x=20, y=20)
window.update()


numEntry = tk.Entry(window, width='10')
numEntry.insert(-1, '300')
numEntry.place(x=wpmLabel.winfo_width() + wpmLabel.winfo_rootx(), y=20)
window.update()

def runLoop():
    global currentIndex, stop, interval, currentState
    while currentIndex < len(speech):
        #when pause button is clicked, it terminates program
        if(stop):
                break
        wordLabel['text'] = speech[currentIndex]
        window.update()
        currentIndex += 1
        time.sleep(interval)
    if(currentIndex == len(speech)):
        startButton['state'] = tk.ACTIVE
        resumeButton['state'] = tk.DISABLED
        pauseButton['state'] = tk.DISABLED
        currentIndex = 0
        currentState += 1
            


#function when user clicks start, pause or resume
def startProg():
    global currentState, currentIndex, stop, interval
    interval = 60 / int(numEntry.get())
    currentState += 1

    #if user wants to continue/start the words 
    if(currentState % 2 != 0):
        #disables buttons
        startButton['state'] = tk.DISABLED
        resumeButton['state'] = tk.DISABLED
        pauseButton['state'] = tk.ACTIVE
        stop = False
        runLoop()
    
    #if user wants to start the words
    else:
        pauseButton['state'] = tk.DISABLED
        resumeButton['state'] = tk.ACTIVE
        stop = True



startButton = tk.Button(window, text="Start", bg="white", fg="green", command=startProg, padx=5, pady=5)
startButton.place(x=numEntry.winfo_width() + numEntry.winfo_rootx(), y=20)
window.update()

resumeButton = tk.Button(window, text="Resume", bg="white", fg="green", command=startProg, padx=5, pady=5, state=tk.DISABLED)
resumeButton.place(x=startButton.winfo_width() + startButton.winfo_rootx(), y=20)
window.update()

pauseButton = tk.Button(window, text="Pause", bg="white", fg="red", command=startProg, padx=5, pady=5, state=tk.DISABLED)
pauseButton.place(x=resumeButton.winfo_width() + resumeButton.winfo_rootx(), y=20)



window.mainloop()





