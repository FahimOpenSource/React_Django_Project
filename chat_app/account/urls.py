from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('sign-in',register, name='sign_in'),
    path('sign-out', sign_out, name='sign_out'),
    path('sign-up', register, name='sign_up'),

    # API URLS
    path('api/all', UserView.as_view()),
    path('api/all/<int:pk>', UserView.as_view()),
    path('api/signup', SignUpView.as_view()),
    path('api/signin', SignInView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]