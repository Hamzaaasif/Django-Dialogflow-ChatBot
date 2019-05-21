from django.urls import path
from .views import home

app_name = "Bot"

urlpatterns = [
    path('', home,name='home'),
]