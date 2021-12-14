from rest_framework.views import APIView
from rest_framework import generics,status 
from rest_framework.response import Response 
from .models import Message
from account.models import Account
from account.exceptions import UnsignedUser
from profile_api.models import Friend
from .serializers import ChatsSerializer,InboxSerializer, MessageSerializer
from rest_framework.parsers import MultiPartParser,FormParser
import cloudinary.uploader

class LoadChatsView(generics.RetrieveAPIView):
    """Loads all inboxes for an account"""

    queryset = Account.objects.all()
    serializer_class = ChatsSerializer
        
    def get_object(self):
        queryset = self.get_queryset()
        try:
            self.request.session['id']
        except KeyError:
            raise UnsignedUser()
        for obj in queryset:
            if obj.id == self.request.session['id']:
                return obj 

class CreateInboxView(generics.RetrieveUpdateAPIView):
    """Creates inboxes from updating the chat field"""
    queryset = Friend.objects.all()
    serializer_class = InboxSerializer
    lookup_url_kwarg = 'pk'

class SendMessageView(generics.CreateAPIView):
    """Creates a message"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class DeleteMessageView(generics.RetrieveDestroyAPIView):
    """Deletes a message"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_url_kwarg = 'pk'    


class UploadView(APIView):
    """uploads files to cloudinary"""

    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        # gets the value(any file like img,jpg,mp3...) of the key `file` 
        file_obj = request.data.get('file')
        # uploads the file to cloudinary and gets back a json response         
        response = cloudinary.uploader.upload(file_obj)
        return Response(response)
     
class DeleteUploadView(APIView):
    """deletes uploaded files from cloudinary requires `public id` and `resource type`"""
    
    # Deletes uploaded assets
    def delete(self,public_id,resource_type):
        response_msg = cloudinary.uploader.destroy(public_id, resource_type= resource_type)
        return Response(response_msg,status=status.HTTP_204_NO_CONTENT)