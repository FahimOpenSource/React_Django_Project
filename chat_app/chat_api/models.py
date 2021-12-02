from django.db import models
from profile_api.models import Friend
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Message(models.Model):

    forwaded_message = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='forwarded')
    text = models.CharField(max_length=700, null=True, blank=True)
    sent_to = models.ForeignKey(Friend, on_delete=models.CASCADE, null=False, blank=False, related_name='received')
    sent_by = models.ForeignKey(Friend, on_delete=models.CASCADE, null=False, blank=False, related_name='sent')
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.JSONField(blank=True, null=True)

    def clean(self):
        # makes sure you can't send a message to yourself 
        if self.sent_to == self.sent_by :
            raise ValidationError({
                'sent_to': ValidationError(_('may not equal to sent_to.'), code='invalid'),
                'sent_by': ValidationError(_('may not equal to sent_by.'), code='invalid'),
            })
        # makes sure you either have a text or a file(response) you want to send or both
        elif not self.text or self.response:
            raise ValidationError({
                'required': ValidationError(_('alteast text or response is required.'))
            })


    def __str__(self):
        return str(self.id)