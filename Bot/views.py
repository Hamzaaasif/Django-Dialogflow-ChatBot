from django.shortcuts import render
import requests

def home(request):
  url='https://api.dialogflow.com/v1/query?v=20150910&contexts=smalltalk&lang=en&query=hey&sessionId=12345&timezone=America/New_York'
  Headers = {
    'Authorization': 'Bearer a5aaf3c137ce49b1ae3710de1528036e',
  } 
  r =requests.get(url, headers=Headers)
  print("The response", r.json()['result']['fulfillment']['speech'])

  # rendering the template in templates folder
  return render(request, "app.html", {'response': r.json()['result']['fulfillment']['speech']})

