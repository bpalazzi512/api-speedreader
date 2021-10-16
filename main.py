import tkinter as tk
import vlc
import time
from pip._vendor import requests
from pip._vendor.requests.models import Response

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()


#first function call
myApi = "1105ab38c7e6453cb1bcb31545fe63e4"
def callFirst():
  endpoint = "https://api.assemblyai.com/v2/transcript"

  json = {
    "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
  }

  headers = {
      "authorization": myApi,
      "content-type": "application/json"
  }

  response = requests.post(endpoint, json=json, headers=headers)

  print(response.json())

#second function to call again
def callAgain():
  endpoint = "https://api.assemblyai.com/v2/transcript/fr8qlzofc-cb34-485a-a0f3-2595777930a3"

  headers = {
      "authorization": myApi,
  }

  response = requests.get(endpoint, headers=headers)
  test = response.json()
  #print(response.json())
  print(test["text"])
  
  

callAgain()
