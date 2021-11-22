from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/<int:pk>', LoadChatsView.as_view()),
    path('api/message',MessageView.as_view()),
    path('api/inbox/', CreateInboxView.as_view()),
    path('api/inbox/<int:pk>', InboxView.as_view()),
    path('api/upload', UploadView.as_view()),
]