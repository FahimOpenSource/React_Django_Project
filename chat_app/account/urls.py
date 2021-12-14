from django.urls import path
from .views import AccountView, AllAccountsView, SignUpView, SignInView


urlpatterns = [ 
    path('api/my-account', AccountView.as_view(), name='account'),
    path('api/all', AllAccountsView.as_view(), name='allaccounts'),
    path('api/sign-up/', SignUpView.as_view(), name='signup'),
    path('api/sign-in/', SignInView.as_view(), name='signin'),
]
