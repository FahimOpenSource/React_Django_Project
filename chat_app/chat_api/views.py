from rest_framework.views import APIView
from rest_framework import generics,status 
from rest_framework.response import Response 
from django.http import Http404
from .models import Inbox,Message
from account.models import Account
from profile_api.models import Friend
from .serializers import ChatsSerializer,InboxSerializer, MessageSerializer

class LoadChatsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = ChatsSerializer
    lookup_url_kwarg = 'pk'

class InboxView(APIView):
    serializer_class = InboxSerializer

    def get(self,request,pk):
        try:
            inbox = Inbox.objects.get(pk=pk)
        except Inbox.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(inbox)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateInboxView(APIView):
    serializer_class = InboxSerializer
    def post(self,request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            account = serializer.validated_data.get('account',None)
            friend = serializer.validated_data.get('friend',None)
            if account == friend.approved_account:
                return Response({'error': 'invalid input'},status=status.HTTP_401_UNAUTHORIZED)
            try:
                Friend.objects.get(account=account,approved_account=friend.approved_account)
            except Friend.DoesNotExist:
                return Response({'detail': 'inbox must be with a friend'},status=status.HTTP_401_UNAUTHORIZED)
            serializer = self.serializer_class(serializer.save())
            return Response(serializer.data, status=status.HTTP_200_OK)

class MessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
