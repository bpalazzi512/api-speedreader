from pip._vendor import requests
from pip._vendor.requests.models import Response
import time
import logging




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

  responseJson = response.json()
  #return (responseJson["status"])
  return response.json()

#second function to call again
def callAgain():
    initalTest = callFirst()
    #while(callFirst() == "queued"):
        #print ("queued")
        #time.sleep(.1)
    endpoint = "https://api.assemblyai.com/v2/transcript/fr8qlzofc-cb34-485a-a0f3-2595777930a3"
    #endpoint = "https://api.assemblyai.com/v2/transcript/"+initalTest["id"]
    logging.debug(initalTest["id"])
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
    print(test["text"])
    return apiText

def normalTestCall():
    endpoint = "https://api.assemblyai.com/v2/transcript/fr8qlzofc-cb34-485a-a0f3-2595777930a3"
    headers = {
    "authorization": "1105ab38c7e6453cb1bcb31545fe63e4",
    }

    response = requests.get(endpoint, headers=headers)
    print(response.json())
  
  
#callFirst()
callAgain()
#normalTestCall()
