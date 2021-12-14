from .models import Account
from .serializers import AccountSerializer, SignInSerializer
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .exceptions import UnsignedUser

class AllAccountsView(generics.ListAPIView):
    """Lists all accounts """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class SignUpView(APIView):
    """creates accounts """

    def get(self,request):
        """Return a list of all users."""
        usernames = [account.username for account in Account.objects.all()]
        return Response(usernames)

    serializer_class = AccountSerializer
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pk = serializer.data['id']
            print(pk)
            request.session['id'] = pk
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInView(APIView):

    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = Account.objects.get(username=username)
            except Account.DoesNotExist:
                return Response({"message":"user not found"}, status=status.HTTP_404_NOT_FOUND)
            
            if not user.check_password(password) :
                return Response({"password":"incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
            else :
                request.session['id'] = user.id
                return Response({"message":"successfull"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """`Gets` , `updates` and `deletes` an account by `id` in stored session"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_object(self):
        queryset = self.get_queryset()
        try:
            self.request.session['id']
        except KeyError:
            raise UnsignedUser()
        for obj in queryset:
            if obj.id == self.request.session['id']:
                return obj 
            

