from .models import *
from .serializers import *
from rest_framework import generics


class SignUpView(generics.ListCreateAPIView):
    """Lists and creates accounts """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """`Gets` , `updates` and `deletes` an account by `id`"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = 'pk'

