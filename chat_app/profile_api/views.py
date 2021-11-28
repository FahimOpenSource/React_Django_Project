from rest_framework import generics, status
from rest_framework.response import Response
from account.models import Account
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *

class ProfileView(generics.RetrieveAPIView):
    """ views a user's profile by id specified in url """

    queryset = Account.objects.all()
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'pk'

class SendFriendRequestView(generics.ListCreateAPIView):
    """Lists and sends a friend request"""

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendRequestView(generics.RetrieveUpdateDestroyAPIView):
    """Lets you update a friend request to either `approve` , `decline` and `delete` it specified by the `pk`"""

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = 'pk'
    
class DeleteFriendView(APIView):
    """Deletes a  friend specified in by `pk`"""

    def delete(self,request,pk):
        try: 
            friend = Friend.objects.get(pk=pk)
        except Friend.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        request = friend.approved_request 
        # gets the pair of friends that was created
        friends = Friend.objects.filter(approved_request=request)
        
        if friends.exists():
            # deletes the pair
            friends.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
