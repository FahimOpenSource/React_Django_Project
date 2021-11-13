from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import generics,status 
from rest_framework.views import APIView
from rest_framework.response import Response 

class AllAccountsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class SignUpView(APIView):
    serializer_class = AccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username',None)
            if username:
                queryset = Account.objects.filter(username=username)

                if queryset.exists():
                    return Response({'error':'username already exists'},status=status.HTTP_401_UNAUTHORIZED)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

# methods to be added put,get,delete
class AccountView(APIView):
    serializer_class = AccountSerializer

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Account = self.get_object(pk)
        Account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
