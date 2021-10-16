import pip._vendor.requests 
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import filedialog
import time
import sys
from pip._vendor import requests
from pip._vendor.requests.models import Response
import time
import logging
import json


myApiToken = "1105ab38c7e6453cb1bcb31545fe63e4"
callAgainWait = 0
#localMyURL = " "
#theId = " "

def callFirst():
  global wait,callAgainWait
  wait = 0
  
  endpoint = "http://api.assemblyai.com/v2/transcript"
  #localMyURL = getMyURL()
  

  json = {
    "audio_url": localMyURL
  }

  headers = {
      "authorization": myApiToken,
      "content-type": "application/json"
  }
  print("POINT 1.5 \n")
  print(json)
  response = requests.post(endpoint, json=json, headers=headers)
  print("POINT 1.8 \n")
  responseJson = response.json()
  #responseJson = json.loads(response.json)
  print("POINT 1.9 \n")

  global theId 
  theId = str(responseJson.get("id"))
  print(theId)
  print("POINT 1.95 \n")
#   while(theId == " "):
#       time.sleep(.1)
#       theId = str(responseJson.get("id"))

  time.sleep(3)
  headers = {
            "authorization": myApiToken
    }
  print(headers)
  print(endpoint)
  response = requests.get(endpoint, headers=headers)
  responseJson = response.json()
  print(responseJson)
  print(" in while ")
  endpoint  = "https://api.assemblyai.com/v2/transcript/" + theId
  print(endpoint)
  while(str(responseJson.get("status"))!= "completed"):
      print(str(responseJson.get("status")))
      time.sleep(3)
      headers = {
      "authorization": myApiToken
      }
      response = requests.get(endpoint, headers=headers)
      responseJson = response.json()
      print(responseJson)
      print(" in while ")

  print("just out of while")
  #return (responseJson["status"])
  wait = 1
  time.sleep(1)
  return response.json()
  #return id

#second function to call again
def callAgain():
    
    print("POINT 1 \n")
    initalTest =  callFirst()
    while(wait == 0 ):
        time.sleep(.5)
    print("POINT 2 \n")
    #while(callFirst() == "queued"):
        #print ("queued")
        #time.sleep(.1)
    #endpoint = "https://api.assemblyai.com/v2/transcript/fr8qlzofc-cb34-485a-a0f3-2595777930a3"
    #endpoint = "https://api.assemblyai.com/v2/transcript/"+initalTest["id"]
    print(theId)
    global endpoint
    endpoint = "http://api.assemblyai.com/v2/transcript/" + theId

    print("POINT 3 \n")
    headers = {
        "authorization": myApiToken,
    }

    response = requests.get(endpoint, headers=headers)
    test = response.json()
    time.sleep(1)
    while(test.get("status")== "queued"):
        response = requests.get(endpoint, headers=headers)
        test = response.json()
        time.sleep(3)
        print("loading")
    print("POINT 4 \n")
    print(response.json())
    apiText = str(test.get("text"))
    #print(test["text"])
    print("APITEXT!!!!!: " + apiText)
    
    return apiText


myURL = " " 
textFromMain = " "

def startProgram(event):
    for i in range (3):
        textBox = tk.Label(text = i+1)
        textBox.pack()
        window.update()
        time.sleep(1)
    
    #telempromter()

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': "1105ab38c7e6453cb1bcb31545fe63e4"}
    response = pip._vendor.requests.post('http://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))
    apiObject = response.json()
    global localMyURL
    localMyURL = apiObject["upload_url"]
    #print('Selected:', filename)
    #print(myURL)

    
    label = tk.Label(text="Your Texts:")
    textFromMain = callAgain()
    
    #textFrom MAIn get text from te main here
    labelTwo = tk.Label(text = textFromMain)
    textBox = tk.Label(text = " ")
    widgetLabel = tk.Label(text="WPM,enter to start")
    entry = tk.Entry()

    label.pack()
    labelTwo.pack()
    widgetLabel.pack()
    entry.pack()
    textBox.pack()

    
    window.bind("<Return>", startProgram)

def getMyURL():
    return localMyURL

window = tk.Tk()
button = tk.Button(window, text='Open', command=UploadAction)
button.pack()
window.mainloop()

# def telempromter():
#     words = len(textFromMain)
#     wpm = int(entry.get())
#     #list = textFromMain.split()
#     for i in range (words):
#         list = textFromMain.split()[i]
#         textBox = tk.Label(text = list)
#         textBox.pack()
#         print(list)
#         window.update()
    
#         time.sleep(1/wpm)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
 )












