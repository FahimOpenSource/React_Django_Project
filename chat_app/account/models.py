from django.db import models
from django.contrib.auth.models import AbstractUser

def validate_string(string):
    """removes whitespace and double spaces in strings"""
    string = string.strip()
    string = " ".join(string.split())
    return string


class Account(AbstractUser):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    active = models.BooleanField(default=True)# needs to go
    last_seen_date = models.DateField(blank=True, null=True)
    last_seen_time = models.TimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.set_password(self.password.strip())
        self.username = validate_string(self.username)
        self.first_name = validate_string(self.first_name)
        self.last_name = validate_string(self.last_name)
        super(Account, self).save(*args, **kwargs)
   
    def __str__(self):
        return str(self.username)



