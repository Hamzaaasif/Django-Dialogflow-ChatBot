from django.shortcuts import render
import requests

SaveChat=[]
botchat=[]

def home(request):
  userpost = 'hey'
  if request.method == "POST":
    userpost =request.POST['myvalue']
  print(userpost)  
  myurl='https://api.dialogflow.com/v1/query?v=20150910&contexts=mayar&lang=en&query='+userpost+'&sessionId=12345&timezone=America/New_York'
  Headers = {
    'Authorization': 'Bearer 9c374562864a43939a83047fa43da137',
  } 
  r =requests.get(myurl, headers=Headers)
  print("The response", r.json()['result']['fulfillment']['speech'])
  SaveChat.append("User: "+userpost)
  SaveChat.append("Bot: "+r.json()['result']['fulfillment']['speech'])
  UserChat={'Chat1': SaveChat}
  #BOTChat={'Bot':UserChat }

  # rendering the template in templates folder
  return render(request, "app.html",UserChat )


