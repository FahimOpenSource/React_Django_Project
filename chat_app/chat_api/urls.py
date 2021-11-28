from django.urls import path
from .views import *


urlpatterns = [ 
    path('api/<int:pk>', LoadChatsView.as_view()),
    path('api/message',MessageView.as_view()),
    path('api/message/<int:pk>',DeleteMessageView.as_view()),
    path('api/inbox/<int:pk>', CreateInboxView.as_view()),
    path('api/upload', UploadView.as_view()),
    path('api/upload/<slug:public_id>/<str:resource_type>', DeleteUploadView.as_view()),

]