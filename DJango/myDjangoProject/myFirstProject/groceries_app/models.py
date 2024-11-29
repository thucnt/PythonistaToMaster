from django.db import models
from django.urls import reverse

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=30)


    def get_absolute_url(self):
        return reverse('userdetail', kwargs={'pk': self.pk})