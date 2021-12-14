from rest_framework import generics, status
from rest_framework.response import Response
from account.models import Account
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from account.exceptions import UnsignedUser

class ProfileView(generics.RetrieveAPIView):
    """ views a user's profile by id """

    queryset = Account.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        try:
            self.request.session['id']
        except KeyError:
            raise UnsignedUser()
        for obj in queryset:
            if obj.id == self.request.session['id']:
                return obj 

class SendFriendRequestView(generics.CreateAPIView):
    """send a friend request"""
    
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendRequestView(generics.RetrieveUpdateDestroyAPIView):
    """Lets you update a friend request to either `approve` , `decline` and `delete` it specified by the `pk`"""

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    
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
