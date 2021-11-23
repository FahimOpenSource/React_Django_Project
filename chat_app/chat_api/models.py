from django.db import models
from account.models import Account
from profile_api.models import Friend

class Inbox(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='chats')
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, blank=False, related_name='friend')
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.account)

class Message(models.Model):
    # one forwd msg at a time
    forwaded_message = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='forwarded')
    text = models.CharField(max_length=700, null=True, blank=False)
    sent_to = models.ForeignKey(Inbox,on_delete=models.CASCADE, null=False, blank=False, related_name='received')
    sent_by = models.ForeignKey(Inbox,on_delete=models.CASCADE, null=False, blank=False, related_name='sent')
    date = models.DateTimeField(auto_now_add=True)
    response = models.JSONField(blank=True,null=True)