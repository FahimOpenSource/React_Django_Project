from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/<int:pk>', ProfileView.as_view(), name='profile'),
    path('api/request/', SendFriendRequestView.as_view(), name='send_request'),
    path('api/request/<int:pk>', FriendRequestView.as_view(), name='view_request'),
    path('api/friend/<int:pk>',DeleteFriendView.as_view(), name='delete_friend')
]