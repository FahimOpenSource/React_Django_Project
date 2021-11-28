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
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendRequestView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = 'pk'
    
class DeleteFriendView(APIView):

    def delete(self,request,pk):
        try: 
            friend = Friend.objects.get(pk=pk)
        except Friend.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        request = friend.approved_request 
        friends = Friend.objects.filter(approved_request=request)
        
        if friends.exists():
            friends.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# class FriendRequestView(APIView):
#     serializer_class = FriendRequestSerializer

#     def get_object(self, pk):
#         try:
#             return FriendRequest.objects.get(pk=pk)
#         except FriendRequest.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         serializer = self.serializer_class(obj)
#         return Response(serializer.data)



#     def put(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         serializer = self.serializer_class(obj, data=request.data)
#         if serializer.is_valid():
#             instance = serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, pk, format=None):
#         request = self.get_object(pk)
#         request.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

