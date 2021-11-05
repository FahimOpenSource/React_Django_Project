from django.urls import path, include
from .views import *

urlpatterns = [ 
    path('sign-in',sign_in, name='sign_in'),
    path('sign-out', sign_out, name='sign_out'),
    path('sign-up', sign_up, name='sign_up'),

    # API URLS
    path('api/all', AccountsView.as_view()),
    path('api/signup', SignUpView.as_view()),
    path('api/signin', SignInView.as_view())
]
 