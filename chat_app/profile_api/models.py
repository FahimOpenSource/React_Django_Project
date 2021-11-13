from django.db import models
from account.models import *

class FriendRequest(models.Model):
    #what if an user that sent the request does not exist
    sent_to = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='received')
    sent_by = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='sent')
    declined = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'from: {self.sent_by} to: {self.sent_to}'

class Friend(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='friends')
    friend = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='friend')
    approved_request = models.ForeignKey(FriendRequest,on_delete=models.CASCADE, blank=False, related_name='approved_request')
    chat = models.BooleanField(default=False)
    # add date time field
    def __str__(self):
        return self.friend

