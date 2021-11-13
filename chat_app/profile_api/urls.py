from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/<int:pk>', ProfileView.as_view()),# view onlyy not changeable
    path('api/send-request/', SendFriendRequestView.as_view()),
    path('api/update-request/<int:pk>', UpdateFriendRequestView.as_view()),
]