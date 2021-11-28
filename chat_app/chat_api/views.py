from rest_framework.views import APIView
from rest_framework import generics,status 
from rest_framework.response import Response 
from .models import Message
from account.models import Account
from profile_api.models import Friend
from .serializers import ChatsSerializer,InboxSerializer, MessageSerializer
from rest_framework.parsers import MultiPartParser,FormParser
import cloudinary.uploader

class LoadChatsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = ChatsSerializer
    lookup_url_kwarg = 'pk'

# class InboxView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Inbox.objects.all()
#     serializer_class = InboxSerializer
#     lookup_url_kwarg = 'pk'      

# class InboxView(APIView):
#     serializer_class = InboxSerializer

#     def get(self,request,pk):
#         try:
#             inbox = Inbox.objects.get(pk=pk)
#         except Inbox.DoesNotExist:
#             return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.serializer_class(inbox)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class CreateInboxView(generics.RetrieveUpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = InboxSerializer
    lookup_url_kwarg = 'pk'

class MessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class DeleteMessageView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_url_kwarg = 'pk'    

class UploadView(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request,format=None):
        file_obj = request.data.get('file')
        print(file_obj)
        upload_data = cloudinary.uploader.upload(file_obj)
        return Response(upload_data)
     
class DeleteUploadView(APIView):

    def delete(self,request,public_id,resource_type):
        response_msg = cloudinary.uploader.destroy(public_id, resource_type= resource_type)
        return Response(response_msg,status=status.HTTP_204_NO_CONTENT)