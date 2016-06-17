from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model):
    user_username = models.CharField(max_length=20 , primary_key=True)
    user_password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    def __str__(self):
        return self.user_username
