from django.db import models
from profile_api.models import Friend
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# class Inbox(models.Model):
#     account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='chats')
#     friend = models.ForeignKey(Friend, on_delete=models.CASCADE, blank=False, related_name='friend')
#     blocked = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.account)

class Message(models.Model):

    forwaded_message = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='forwarded')
    text = models.CharField(max_length=700, null=True, blank=True)
    sent_to = models.ForeignKey(Friend, on_delete=models.CASCADE, null=False, blank=False, related_name='received')
    sent_by = models.ForeignKey(Friend, on_delete=models.CASCADE, null=False, blank=False, related_name='sent')
    date = models.DateTimeField(auto_now_add=True)
    response = models.JSONField(blank=True, null=True)

    def clean(self):
        if self.sent_to == self.sent_by :
            raise ValidationError({
                'sent_to': ValidationError(_('may not equal to sent_to.'), code='invalid'),
                'sent_by': ValidationError(_('may not equal to sent_by.'), code='invalid'),
            })
        elif not self.text or self.response:
            raise ValidationError({
                'required': ValidationError(_('alteast text or response is required.'))
            })


    def __str__(self):
        return str(self.id)