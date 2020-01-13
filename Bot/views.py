from django.shortcuts import render
import requests

SaveChat=[]
def home(request):
  userpost = 'Start conversion'
  if request.method == "POST":
    userpost =request.POST['myvalue']
  print(userpost)  
  myurl='https://api.dialogflow.com/v1/query?v=20150910&contexts=mayar&lang=en&query='+userpost+'&sessionId=12345&timezone=America/New_York'
  Headers = {
    'Authorization': 'Bearer 9c374562864a43939a83047fa43da137',
  } 
  r =requests.get(myurl, headers=Headers)
  SaveChat.append("User: "+userpost)
  SaveChat.append("Bot: "+r.json()['result']['fulfillment']['speech'])
  UserChat={'Chat1': SaveChat}
  return render(request, "app.html",UserChat )


