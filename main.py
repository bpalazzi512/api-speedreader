from pip._vendor import requests
from pip._vendor.requests.models import Response
import time
import logging
from window import getMyURL




#first function call
myApi = "1105ab38c7e6453cb1bcb31545fe63e4"
id =" "

def callFirst():
  endpoint = "https://api.assemblyai.com/v2/transcript"
  localMyURL = getMyURL()
  

  json = {
    "audio_url": localMyURL
  }

  headers = {
      "authorization": myApi,
      "content-type": "application/json"
  }

  response = requests.post(endpoint, json=json, headers=headers)

  responseJson = response.json()
  id =responseJson["id"]
  #return (responseJson["status"])
  return response.json()

#second function to call again
def callAgain():
    print("POINT 1 \n")
    initalTest = callFirst()
    #while(callFirst() == "queued"):
        #print ("queued")
        #time.sleep(.1)
    #endpoint = "https://api.assemblyai.com/v2/transcript/fr8qlzofc-cb34-485a-a0f3-2595777930a3"
    endpoint = "https://api.assemblyai.com/v2/transcript/"+initalTest["id"]
    headers = {
        "authorization": myApi,
    }

    response = requests.get(endpoint, headers=headers)
    test = response.json()
    while(test["status"]== "queued"):
        response = requests.get(endpoint, headers=headers)
        test = response.json()
        time.sleep(.1)
    #print(response.json())
    apiText = test["text"]
    #print(test["text"])
    print("APITEXT!!!!!: " + apiText)
    return apiText



  

