from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [ 
    path('sign-in',sign_in, name='sign_in'),
    path('sign-out', sign_out, name='sign_out'),
    path('sign-up', sign_up, name='sign_up'),

    # API URLS
    path('api/all', AccountsView.as_view()),
    path('api/signup', SignUpView.as_view()),
    path('api/signin', SignInView.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]