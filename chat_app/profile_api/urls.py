from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/<int:pk>', ProfileView.as_view()),
    path('api/request/', SendFriendRequestView.as_view()),
    path('api/request/<int:pk>', FriendRequestView.as_view()),
    path('api/friend/<int:pk>',DeleteFriendView.as_view())
]