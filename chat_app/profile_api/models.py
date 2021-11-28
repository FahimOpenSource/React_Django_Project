from django.db import models
from account.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FriendRequest(models.Model):
    sent_to = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='received')
    sent_by = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='sent')
    declined = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.sent_to == self.sent_by :
            raise ValidationError({
                'sent_to': ValidationError(_('may not equal to sent_to.'), code='invalid'),
                'sent_by': ValidationError(_('may not equal to sent_by.'), code='invalid'),
            })
        elif self.declined and self.approved:
            raise ValidationError({
                'approved': ValidationError(_('may not equal to approved.'), code='invalid'),
                'declined': ValidationError(_('may not equal to declined.'), code='invalid')
            })

    def __str__(self):
        return f'from: {self.sent_by} to: {self.sent_to}'

class Friend(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='friends')
    friend_account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, related_name='account')
    approved_request = models.ForeignKey(FriendRequest,on_delete=models.CASCADE, blank=False, related_name='approved_request')
    chat = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.account == self.friend_account:
            raise ValidationError({
                'friend account': ValidationError(_('may not equal to your account'), code='invalid')
            })

    def __str__(self):
        return str(self.friend_account)

