from django.db import models
from django.contrib.auth.models import AbstractUser

# make sure to hash the password before saving the model
class Account(AbstractUser):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    active = models.BooleanField(default=True)
    last_seen_date = models.DateField(blank=True, null=True)
    last_seen_time = models.TimeField(blank=True, null=True)

    def clean(self):
        self.set_password(self.password)
   
    def __str__(self):
        return str(self.username)



